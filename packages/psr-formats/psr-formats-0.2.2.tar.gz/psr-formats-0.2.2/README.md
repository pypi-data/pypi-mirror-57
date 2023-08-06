### psr-formats

Formats for loading and saving data used in pulsar data processing.

Supported formats:
  - DADA

### Usage

```python
>>> from psr_formats import DADAFile
>>> dada_file = DADAFile("path/to/dada.dump").load_data()
>>> dada_file["NCHAN"]
'1'
>>> dada_file.nchan
1
>>> dada_file.npol
2
>>> dada_file.sampling_rate
<Quantity 0.025 us>
>>> dada_file.data.shape
(3107730, 1, 2) # ndat, nchan, npol
>>> new_dada_file = DADAFile("new.dump")
>>> new_dada_file.data = dada_file.data
>>> new_dada_file.dump_data()
'new.dump'
```

### Testing

```
poetry run python -m unittest
```
