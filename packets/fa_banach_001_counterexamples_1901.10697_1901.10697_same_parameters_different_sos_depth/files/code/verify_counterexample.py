#!/usr/bin/env python3
"""Exact verifier for two (26,13) ETFs with different SOS hierarchy depth.

All mathematical checks after graph6 decoding use integer or SymPy rational
arithmetic.  The only external data are the two embedded graph6 strings, the
first two entries of Brendan McKay's catalogue of the ten
SRG(26,10,3,4) graphs.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import networkx as nx
import numpy as np
import sympy as sp


CUT_GRAPH6 = "Y}qCCmMlDSIPRCXPKSQhHQooE^`E`pHQoQuHBRc_oo}EHSMILOkEWXB_"
NONCUT_GRAPH6 = "Y}qCCmMlDSIQRBWokcadAROKE]XEXPHecTJ_AlWGooveDEcISRDEX_p_"

N = 26
R = 13


def adjacency_from_graph6(graph6: str) -> np.ndarray:
    graph = nx.from_graph6_bytes(graph6.encode("ascii"))
    return nx.to_numpy_array(graph, nodelist=range(N), dtype=np.int64)


def validate_srg_and_seidel(adjacency: np.ndarray) -> np.ndarray:
    assert adjacency.shape == (N, N)
    assert np.array_equal(adjacency, adjacency.T)
    assert np.array_equal(np.diag(adjacency), np.zeros(N, dtype=np.int64))
    assert np.all(adjacency.sum(axis=1) == 10)

    common = adjacency @ adjacency
    for i in range(N):
        for j in range(i + 1, N):
            assert common[i, j] == (3 if adjacency[i, j] else 4)

    seidel = np.ones((N, N), dtype=np.int64) - np.eye(N, dtype=np.int64) - 2 * adjacency
    assert np.array_equal(seidel @ seidel, 25 * np.eye(N, dtype=np.int64))
    assert np.trace(seidel) == 0
    # Therefore S has eigenvalues +5 and -5, each with multiplicity 13, and
    # X=I+S/5=2P_+ is an ETF Gram matrix of rank 13.
    return seidel


def exact_sign_lines(seidel: np.ndarray) -> list[tuple[int, ...]]:
    """Enumerate all sign lines in ker(S-5I), normalized by z[0]=1.

    A rational nullspace basis is restricted to 13 pivot coordinates.  Every
    vector in the 13-dimensional eigenspace is uniquely determined by its
    values on those coordinates, so enumerating their 2^13 sign assignments
    is exhaustive.  Reconstruction is performed with one common integer
    denominator.
    """

    kernel_matrix = sp.Matrix((seidel - 5 * np.eye(N, dtype=np.int64)).tolist())
    basis_vectors = kernel_matrix.nullspace()
    assert len(basis_vectors) == R
    basis = sp.Matrix.hstack(*basis_vectors)

    _, pivot_rows = basis.T.rref()
    assert len(pivot_rows) == R
    restriction = basis[list(pivot_rows), :]
    assert restriction.det() != 0
    reconstruction = basis * restriction.inv()

    common_denominator = 1
    for value in reconstruction:
        common_denominator = sp.ilcm(common_denominator, value.q)
    reconstruction_integer = np.array(
        [[int(common_denominator * reconstruction[i, j]) for j in range(R)] for i in range(N)],
        dtype=np.int64,
    )

    lines: set[tuple[int, ...]] = set()
    for signs in itertools.product((-1, 1), repeat=R):
        numerator = reconstruction_integer @ np.asarray(signs, dtype=np.int64)
        if not np.all(np.abs(numerator) == common_denominator):
            continue
        vector = numerator // common_denominator
        assert np.array_equal(seidel @ vector, 5 * vector)
        if vector[0] < 0:
            vector = -vector
        lines.add(tuple(int(value) for value in vector))

    return sorted(lines)


def feature_labels() -> list[str]:
    return ["constant"] + [f"({i},{j})" for i in range(N) for j in range(i + 1, N)]


def feature_matrix(lines: list[tuple[int, ...]]) -> sp.Matrix:
    rows: list[list[int]] = []
    for line in lines:
        row = [1]
        row.extend(line[i] * line[j] for i in range(N) for j in range(i + 1, N))
        rows.append(row)
    return sp.Matrix(rows)


def target_features(seidel: np.ndarray) -> sp.Matrix:
    values: list[sp.Rational] = [sp.Rational(1)]
    values.extend(sp.Rational(int(seidel[i, j]), 5) for i in range(N) for j in range(i + 1, N))
    return sp.Matrix(values)


def line_digest(lines: list[tuple[int, ...]]) -> str:
    encoded = "\n".join("".join("+" if x == 1 else "-" for x in line) for line in lines).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify_cut_case(seidel: np.ndarray, lines: list[tuple[int, ...]]) -> dict[str, object]:
    assert len(lines) == 130
    outer_sum = np.zeros((N, N), dtype=np.int64)
    for line in lines:
        vector = np.asarray(line, dtype=np.int64)
        outer_sum += np.outer(vector, vector)

    # X=I+S/5, so uniform averaging over the 130 sign lines is exactly X.
    assert np.array_equal(5 * outer_sum, len(lines) * (5 * np.eye(N, dtype=np.int64) + seidel))
    return {
        "sign_line_count": len(lines),
        "sign_line_sha256": line_digest(lines),
        "exact_outer_sum_identity": "5*sum(zz^T)=130*(5I+S)",
        "cut_decomposition_weights": "uniform 1/130",
    }


def independent_feature_columns(matrix: sp.Matrix) -> list[int]:
    selected: list[int] = []
    rank = 0
    for column in range(matrix.cols):
        trial = matrix[:, selected + [column]]
        trial_rank = trial.rank()
        if trial_rank > rank:
            selected.append(column)
            rank = trial_rank
        if rank == matrix.rows:
            break
    assert rank == matrix.rows
    return selected


def verify_noncut_case(seidel: np.ndarray, lines: list[tuple[int, ...]]) -> dict[str, object]:
    assert len(lines) == 14
    features = feature_matrix(lines)
    assert features.rank() == 14
    target = target_features(seidel)

    selected = independent_feature_columns(features)
    square_system = features[:, selected].T
    selected_target = target[selected, :]
    weights = square_system.inv() * selected_target

    # Check the representation against every one of the 326 affine
    # coordinates, not only the 14 coordinates used to solve for it.
    assert features.T * weights == target
    expected = [sp.Rational(-3, 10)] + [sp.Rational(1, 10)] * 13
    assert sorted(weights) == expected

    negative_index = next(index for index, value in enumerate(weights) if value < 0)
    labels = feature_labels()
    return {
        "sign_line_count": len(lines),
        "sign_line_sha256": line_digest(lines),
        "outer_product_feature_rank": features.rank(),
        "selected_affine_coordinates": [labels[index] for index in selected],
        "unique_affine_weights": [str(value) for value in weights],
        "negative_weight_index": negative_index,
        "negative_weight_sign_line": list(lines[negative_index]),
        "noncut_reason": "the unique affine representation has one weight -3/10",
    }


def run_verification() -> dict[str, object]:
    cut_adjacency = adjacency_from_graph6(CUT_GRAPH6)
    noncut_adjacency = adjacency_from_graph6(NONCUT_GRAPH6)
    cut_seidel = validate_srg_and_seidel(cut_adjacency)
    noncut_seidel = validate_srg_and_seidel(noncut_adjacency)

    cut_lines = exact_sign_lines(cut_seidel)
    noncut_lines = exact_sign_lines(noncut_seidel)

    result = {
        "arithmetic": "exact integer and SymPy rational arithmetic after graph6 decoding",
        "parameters": {"N": N, "r": R, "coherence": "1/5"},
        "cut_case": {
            "graph6": CUT_GRAPH6,
            **verify_cut_case(cut_seidel, cut_lines),
            "largest_generalized_elliptope_degree": 26,
        },
        "noncut_case": {
            "graph6": NONCUT_GRAPH6,
            **verify_noncut_case(noncut_seidel, noncut_lines),
            "largest_generalized_elliptope_degree_upper_bound": 24,
        },
        "conclusion": "same (N,r)=(26,13), different largest generalized-elliptope degree",
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()

    result = run_verification()
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.write_certificate is not None:
        args.write_certificate.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

