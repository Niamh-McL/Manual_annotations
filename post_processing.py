# Filter manually annotated segments with criteria

# minimum event duration (1s)  (define function in processes.py and call in post-processing.py)
for event in labelled_events:
  if duration < 1:
    delete(event)
  else:
    continue

# inter-event interval (define function in processes.py and call in post-processing.py)
for event in labelled_events:
  if event[n, onset+duration] - event[n-1, onset] < 1:
    combine events
  else:
    continue
