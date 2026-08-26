#!/usr/bin/env python3
"""Exact verifier and source-question crop helper for the 2506.02913 packet."""

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

import sympy as sp


def verify() -> None:
    theta, t = sp.symbols("theta t", real=True)
    epsilon = sp.Rational(13, 20)
    scale = sp.Rational(1, 2)
    cosine = -sp.Rational(1, 5)
    sine = 2 * sp.sqrt(6) / 5

    radius = 1 + epsilon * sp.cos(2 * theta)
    radius_prime = sp.diff(radius, theta)
    q = sp.exp(-sp.I * theta) * (
        1 / radius + sp.I * radius_prime / radius**2
    )

    substitutions = {
        sp.cos(theta): cosine,
        sp.sin(theta): sine,
        sp.cos(2 * theta): -sp.Rational(23, 25),
        sp.sin(2 * theta): -4 * sp.sqrt(6) / 25,
    }
    radius_0 = sp.Rational(201, 500)
    q_0 = sp.simplify(sp.expand_complex(q).subs(substitutions))
    eta_0 = radius_0 * (cosine + sp.I * sine)
    zeta_0 = scale * eta_0
    z_0 = sp.simplify(zeta_0 + (1 - scale**2) / (scale * q_0))
    expected_z_0 = (
        sp.Rational(8811237, 43873750)
        + sp.I * sp.Rational(4319088, 21936875) * sp.sqrt(6)
    )
    assert sp.simplify(z_0 - expected_z_0) == 0

    x_0, y_0 = sp.re(z_0), sp.im(z_0)
    modulus_squared = sp.simplify(x_0**2 + y_0**2)
    radial_at_z = sp.simplify(
        1 + epsilon * (x_0**2 - y_0**2) / modulus_squared
    )
    gauge_squared = sp.factor(modulus_squared / radial_at_z**2)
    assert modulus_squared == sp.Rational(598702419, 2193687500)
    assert radial_at_z == sp.Rational(140986860969, 260066040500)
    assert gauge_squared == sp.Rational(
        456889764289102564, 492000073411354561
    )
    assert gauge_squared < 1

    zeta = t * sp.exp(sp.I * theta)
    gauge = t / radius
    B = sp.simplify(gauge * q * (zeta - z_0) + 1 - gauge**2)
    point_subs = dict(substitutions)
    point_subs[t] = scale * radius_0
    B_0 = sp.simplify(sp.expand_complex(B).subs(point_subs))
    assert B_0 == 0

    B_t = sp.simplify(sp.expand_complex(sp.diff(B, t)).subs(point_subs))
    B_theta = sp.simplify(
        sp.expand_complex(sp.diff(B, theta)).subs(point_subs)
    )
    assert B_t == -sp.Rational(1000, 201) + sp.I * sp.Rational(
        26000, 40401
    ) * sp.sqrt(6)
    assert B_theta == sp.Rational(1825018, 7054899) * sp.sqrt(
        6
    ) - sp.I * sp.Rational(8776, 35099)

    jacobian = sp.factor(
        sp.re(B_t) * sp.im(B_theta) - sp.im(B_t) * sp.re(B_theta)
    )
    assert jacobian == sp.Rational(23285456000, 95008324833)
    assert jacobian > 0

    print(f"z_0 = {z_0}")
    print(f"m_D(z_0)^2 = {gauge_squared} < 1")
    print(f"B_D(zeta_0,z_0) = {B_0}")
    print(f"Jacobian = {jacobian} > 0")
    print("all exact checks passed")


def crop_question(source_pdf: Path, output_png: Path) -> None:
    from PIL import Image

    output_png.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary_directory:
        prefix = Path(temporary_directory) / "page"
        subprocess.run(
            [
                "pdftoppm",
                "-f",
                "27",
                "-l",
                "27",
                "-png",
                "-r",
                "180",
                str(source_pdf),
                str(prefix),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        rendered = Image.open(f"{prefix}-27.png")
        width, height = rendered.size
        # Remark 7.3 and its question, with enough surrounding context.
        crop = rendered.crop(
            (int(0.075 * width), int(0.315 * height), int(0.93 * width), int(0.555 * height))
        )
        crop.save(output_png)
        print(f"wrote crop {output_png} ({crop.width}x{crop.height})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-pdf", type=Path)
    parser.add_argument("--crop-output", type=Path)
    arguments = parser.parse_args()
    verify()
    if arguments.source_pdf or arguments.crop_output:
        if not arguments.source_pdf or not arguments.crop_output:
            parser.error("--source-pdf and --crop-output must be supplied together")
        crop_question(arguments.source_pdf, arguments.crop_output)


if __name__ == "__main__":
    main()
