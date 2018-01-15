MetPy Contributions
===================

0.7
---

**[PR #620: Rename Convergence Functions to Divergence](https://github.com/Unidata/MetPy/pull/620)**

- A simple rename of the "convergence" functions to "divergence," which is actually what was being calculated
- Corresponding tests and docstrings also updated
- A good first issue that helped me figure out the contribution process

**[PR #621: Add a Thickness Calculation](https://github.com/Unidata/MetPy/pull/621)**

- A thickness calculation (using the hypsometric equation) to meet a feature requested in [issue #295](https://github.com/Unidata/MetPy/issues/295)
- A good first experience in writing a calculation with documentation for an open-source project, along with unit testing
- Also a good experience in figuring out how to do a git rebase!

https://github.com/Unidata/MetPy/blob/v0.7.0/metpy/calc/thermo.py#L1589-L1712

https://github.com/Unidata/MetPy/blob/v0.7.0/metpy/calc/tests/test_thermo.py#L773-L816

**[PR #669: Add a Mixing Ratio from RH Calculation](https://github.com/Unidata/MetPy/pull/669)**

- A calculation to convert from relative humidity to mixing ratio, given temperature and pressure data.
- Came about in discussions to help fully satisfy the request of [issue #295](https://github.com/Unidata/MetPy/issues/295)

https://github.com/Unidata/MetPy/blob/v0.7.0/metpy/calc/thermo.py#L810-L845

**[PR #677: Update to Treat RH as a Unitless Ratio in Existing Functions](https://github.com/Unidata/MetPy/pull/677)

- A series of modifications to treat relative humidity as a unitless ratio consistently throughout the library
- Came about in discussions in the code review of [PR #669](https://github.com/Unidata/MetPy/pull/669)

Under Review
------------

**[PR #695: Add Batch of Functions for Brunt-Väisälä Frequency and Period](https://github.com/Unidata/MetPy/pull/695)**

**[PR #707: Force `mixing_ratio_from_relative_humidity` to return dimensionless](https://github.com/Unidata/MetPy/pull/707)**