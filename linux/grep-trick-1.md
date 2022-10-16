# This is a grep trick, for finding cheese

```{bash}
export $CHEESEE == "emmenthaler"

grep -r "${CHEESE}"

```

This grep format will call the variable CHEESE and search for its value, 'emmenthaler'.
If you use single quotes instaed, it will search for the string '${CHEESE}', which is
probably not what you want.
