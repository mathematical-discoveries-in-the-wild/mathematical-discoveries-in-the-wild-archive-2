# Verification record

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_cutoff.py
```

Output on 2026-08-11:

```text
certified_even_dimensions=421
range=158..998
weakest_certificate=n=160,t=23,lower_margin=0.0002579293062736265197855532028815123069993598654175701890665718930248561404582099001595
first_t_choices=158:26,160:23,162:26,164:23,166:27,168:23,170:27,172:24,174:27,176:24,178:28,180:24
last_t_choices=976:62,978:53,980:62,982:53,984:62,986:53,988:62,990:53,992:62,994:53,996:63,998:53
```

The checker uses `mpmath.iv` interval arithmetic at 80 decimal digits. A pair
`(n,t)` is accepted only when `t >= 4`, `n >= 4t`, all preliminary lower
bounds are positive, the completed-square radicand has positive lower
endpoint, and the lower endpoint of the final contradiction margin is
strictly positive. No ordinary floating-point sign decision is used to accept
a certificate.

