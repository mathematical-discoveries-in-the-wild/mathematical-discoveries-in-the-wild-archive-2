# Exact GAP computations for arXiv:2210.16262, Questions 6.2 and 6.4.

AMZA := function(G)
    local tbl, irr, sizes, n, total, i, j, s, a;
    if IsAbelian(G) then
        return 1;
    fi;
    tbl := CharacterTable(G);
    irr := Irr(tbl);
    sizes := SizesConjugacyClasses(tbl);
    n := Size(G);
    total := 0;
    for i in [1..Length(irr)] do
        for j in [1..Length(irr)] do
            s := Sum([1..Length(sizes)],
                c -> sizes[c]^2 * irr[i][c] * ComplexConjugate(irr[j][c]));
            a := Sqrt(s * ComplexConjugate(s));
            total := total + irr[i][1] * irr[j][1] * a;
        od;
    od;
    return total / n^2;
end;

ASS := function(G)
    local tbl, irr, sizes, n;
    if IsAbelian(G) then
        return 1;
    fi;
    tbl := CharacterTable(G);
    irr := Irr(tbl);
    sizes := SizesConjugacyClasses(tbl);
    n := Size(G);
    return Sum(irr, chi -> chi[1]^2 *
        Sum([1..Length(sizes)], c ->
            sizes[c]^2 * chi[c] * ComplexConjugate(chi[c]))) / n^2;
end;

ScanDerived := function(firstOrder, lastOrder)
    local n, count, id, G, D, aG, aD;
    count := 0;
    for n in [firstOrder..lastOrder] do
        if not SmallGroupsAvailable(n) then
            continue;
        fi;
        Print("PROGRESS_DERIVED order=", n, " groups=", NumberSmallGroups(n), "\n");
        for id in [1..NumberSmallGroups(n)] do
            G := SmallGroup(n,id);
            D := DerivedSubgroup(G);
            if not IsAbelian(D) then
                count := count + 1;
                aG := AMZA(G);
                aD := AMZA(D);
                if aD > aG then
                    Print("COUNTER_DERIVED G=", [n,id],
                          " Gdesc=", StructureDescription(G),
                          " Dsize=", Size(D),
                          " Ddesc=", StructureDescription(D),
                          " AMZA_G=", aG,
                          " AMZA_D=", aD, "\n");
                    return [G,D,aG,aD];
                fi;
            fi;
        od;
    od;
    Print("NO_DERIVED_COUNTEREXAMPLE candidates=", count,
          " orders=", firstOrder, "..", lastOrder, "\n");
    return fail;
end;

ScanNormalHall := function(firstOrder, lastOrder)
    local n, count, id, G, primes, k, S, H, Q, aG, aQ, normals;
    count := 0;
    for n in [firstOrder..lastOrder] do
        if not SmallGroupsAvailable(n) or Length(Set(FactorsInt(n))) < 2 then
            continue;
        fi;
        Print("PROGRESS_HALL order=", n, " groups=", NumberSmallGroups(n), "\n");
        for id in [1..NumberSmallGroups(n)] do
            G := SmallGroup(n,id);
            primes := Set(FactorsInt(n));
            normals := [];
            if IsSolvableGroup(G) then
                for k in [1..Length(primes)-1] do
                    for S in Combinations(primes,k) do
                        H := HallSubgroup(G,S);
                        if IsNormal(G,H) then
                            Add(normals,H);
                        fi;
                    od;
                od;
            else
                normals := Filtered(NormalSubgroups(G), H ->
                    Size(H) > 1 and Size(H) < n and Gcd(Size(H),Index(G,H)) = 1);
            fi;
            if Length(normals) > 0 then
                aG := fail;
                for H in normals do
                    Q := FactorGroup(G,H);
                    # Abelian quotients have AMZA=1 and cannot violate the
                    # inequality, since every amenability constant is >= 1.
                    if not IsAbelian(Q) then
                        count := count + 1;
                        if aG = fail then
                            aG := AMZA(G);
                        fi;
                        aQ := AMZA(Q);
                        if aQ > aG then
                            Print("COUNTER_HALL G=", [n,id],
                                  " Gdesc=", StructureDescription(G),
                                  " Nsize=", Size(H),
                                  " Ndesc=", StructureDescription(H),
                                  " Qsize=", Size(Q),
                                  " Qdesc=", StructureDescription(Q),
                                  " AMZA_G=", aG,
                                  " AMZA_Q=", aQ, "\n");
                            return [G,H,Q,aG,aQ];
                        fi;
                    fi;
                od;
            fi;
        od;
    od;
    Print("NO_HALL_COUNTEREXAMPLE candidates=", count,
          " orders=", firstOrder, "..", lastOrder, "\n");
    return fail;
end;

ScanSharpNonNilpotent := function(firstOrder, lastOrder)
    local n, id, G, lower, aG, candidates, full;
    candidates := 0;
    full := 0;
    for n in [firstOrder..lastOrder] do
        if not SmallGroupsAvailable(n) then
            continue;
        fi;
        Print("PROGRESS_SHARP order=", n, " groups=", NumberSmallGroups(n), "\n");
        for id in [1..NumberSmallGroups(n)] do
            G := SmallGroup(n,id);
            if not IsNilpotentGroup(G) then
                candidates := candidates + 1;
                lower := ASS(G);
                if lower <= 7/4 then
                    full := full + 1;
                    aG := AMZA(G);
                    if aG = 7/4 then
                        Print("COUNTER_SHARP G=", [n,id],
                              " Gdesc=", StructureDescription(G),
                              " ASS=", lower,
                              " AMZA_G=", aG, "\n");
                        return [G,aG];
                    fi;
                fi;
            fi;
        od;
    od;
    Print("NO_NONNILPOTENT_SHARP candidates=", candidates,
          " full_amza=", full,
          " orders=", firstOrder, "..", lastOrder, "\n");
    return fail;
end;

Print("GAP_VERSION ", GAPInfo.Version, "\n");
if not IsBound(MODE) or MODE = "known" then
    for pair in [[6,1],[8,3],[24,12],[32,43],[96,204],[192,1022]] do
        if pair[2] <= NumberSmallGroups(pair[1]) then
            Print("KNOWN ", pair, " ", AMZA(SmallGroup(pair[1],pair[2])), "\n");
        fi;
    od;
elif MODE = "derived" then
    ScanDerived(FIRST,LAST);
elif MODE = "hall" then
    ScanNormalHall(FIRST,LAST);
elif MODE = "sharp" then
    ScanSharpNonNilpotent(FIRST,LAST);
else
    Error("usage: known | derived FIRST LAST | hall FIRST LAST | sharp FIRST LAST");
fi;
QUIT;
