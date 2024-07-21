# Work in Progress
This repo is still in work and not finished yet.


# TikTok-Statistics | Translations

The base language is English and can be found [here](languages/en.yaml).

## Languages

-   [English | Base](en.yaml)
-   [German](de.yaml)

(If you want to translate into a new language, then simply create a Pull request with a new file)

## Editing an existing translation

If you want to edit an existing translation (Fixing typos, updating it to a newer version, etc), you can just use the github file editor to edit the file.

-   Click the language you want to edit from the list above
-   Click the small "edit" symbol on the top right

<img src="https://i.imgur.com/gZnUQoe.png" alt="edit symbol" width="200">

-   Do the changes you wish to do (Be sure **not** to translate placeholders! For example, `{variable} minutes` should get `{variable} minuten` and **not** `{variable} Minuten`!)

-   Click "Propose Changes"

<img src="https://i.imgur.com/KT9ZFp6.png" alt="propose changes" width="200">

-   Click "Create pull request"

<img src="https://i.imgur.com/oVljvRE.png" alt="create pull request" width="200">

-   I will review your changes and make comments, and eventually merge them! Be sure to regulary check the created pull request for comments.

### Rules for editing

- Do not change any placeholders, for example `{language}`. Those are always indicated by the braces.

- Do not change any keywords, here you're allowed to translate `"Value"` but not the keyword.
```yaml
keyword: "Value"
```

- Always let the Values in quotes, but never quote the keywords

- Do not change the indentation. Also do not change the group seperation. 
```yaml
group:
  keyword: "Value"
```
