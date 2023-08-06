# vin-parser
Library that provides functions to work with VIN strings.

## Install
vin-parser is available on PyPI and can be installed using pip.

`$ pip install vin-parser`

## Usage
All the public functions are exported to the package namespace. We'll alias it as vp in the following examples.

`>>> import vin_parser as vp`
<!--
Example usage with some fakey VINS.
Show wmi, vds for lowercase VINS
-->

The functions `check_no`, `seq_no`, `wmi`, `vds` and `vis` return parts of the VIN string.
```python3
>>> vin = "1GYFK63878R248711"
>>> vp.check_no(vin)
'7'
```
Function `check_no` returns the VIN check digit, i.e. position 9 in the VIN string. It returns for all VINs, even for those that don't use the check digit schema.

```python3
>>> vp.wmi(vin)
'1GY'
>>> vp.vds(vin)
'FK6387'
```
Lowercase VINs are accepted:
```python3
>>> vp.vis(vin.lower())
'8R248711'
```

`check_valid`, `is_valid` and `small_manuf` are predicate functions, i.e. functions that return True or False.
`check_valid` returns True if the VIN's check digit matches the computed value.
`is_valid` returns True if the provided VIN is valid. Because the use of VIN check digit is not adopted worldwide, the check_valid test is not performed when verifing the validity of a VIN.

Functions `continent`, `country`, `year` and `manuf` parse the VIN and return the values. year returns a positive integer, while the others return a string with their name.
```python3
>>> vp.country(vin)
'United States'
>>> vp.year(vin)
2008
>>> vp.manuf(vin)
'General Motors USA'
```

Function `parse` calls all the other functions and returns the results in a dict if the provided VIN is valid.
Function `online_parse` queries the nhtsa api with the provided VIN. Empty values are removed from the response and the rest are returned in a python dict. No other transformations are performed on the keys or values.
Note that, unlike `parse`, `online_parse` doesn't check if the VIN is valid before sending it to the remote server.

The `CHARS` constant is a sorted string with all the valid characters of a VIN: A to Z, 1 to 9 and 0, except for I, O and Q.

