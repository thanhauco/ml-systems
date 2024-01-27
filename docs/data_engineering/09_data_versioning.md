# Data Versioning

## "Code is Versioned. Why isn't Data?"
You check out `git checkout v1.0` of your code. But if it reads from a database that has changed, you can't reproduce the bug.

## DVC (Data Version Control)
Git is for text. DVC is for large files.
-   **Mechanism**:
    1.  Calculates MD5 hash of your `data.csv`.
    2.  Renames file to `hash`. Stores in S3.
    3.  Creates a small text file `data.csv.dvc` containing the hash.
    4.  You checking `data.csv.dvc` into Git.

## LakeFS / Project Nessie
"Git for your Data Lake".
-   Branching: `lakefs branch create feature-1`.
-   Isolation: Write to `feature-1`. Production readers on `main` don't see it.
-   Merge: Atomic promote of the data.

## Time Travel in Delta Lake
Stored as a transaction log (`_delta_log`).
```sql
SELECT * FROM events VERSION AS OF '2023-01-01'
```
Allows reverting accidental deletes or debugging "What did the model see yesterday?".
