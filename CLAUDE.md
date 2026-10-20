# CLAUDE.md

Personal academic homepage (Jekyll, Academic Pages template), served from GitHub Pages on push to `main`.

Publications and talks are maintained as Excel sheets in `scripts/`, turned into HTML by a script, and pasted into a page. The `markdown_generator/` and `_publications/`/`_talks/` collections are unused template leftovers — don't edit them.

## General rules

- Excel is the source of truth. Add new rows at the **top** of the sheet (row 2): the scripts keep sheet order within a year/section.
- Edit `.xlsx` files with openpyxl (preserve existing rows/styles; extend `ws.auto_filter.ref` to cover new rows). Verify the original rows are unchanged afterwards.
- Run scripts from inside `scripts/` (they use relative paths), then delete the generated `scripts/my_*.html` — it's not committed.
- Before pasting, the regenerated block should differ from the page only by the new entries. If the diff is larger, stop and investigate rather than committing a reshuffle.
- Some files use CRLF line endings (both `scripts/*.py`, `_pages/news.md`, and several other `_pages/*.md`). Preserve the existing line endings when editing (e.g. read/write in binary mode); a diff that touches every line means they were converted.
- Confirm missing or ambiguous details with the user before editing. Don't commit or push until asked.

## Adding publications

1. Get details from Google Scholar (`https://scholar.google.com/citations?user=jnoUuGcAAAAJ&view_op=list_works&sortby=pubdate`) and the arXiv abstract page (authoritative for exact title, author order, and acceptance comments).
2. Add rows to `scripts/my_publications.xlsx`:
   - `pub_year`: year of publication.
   - `keyword`: `/`-separated, typically `NLP` + 1–4 of the existing categories (Indic, Multilingual, LM, Speech, Reasoning, Translation, Transliteration, ASR, Crowdsourcing, Embeddings, Evaluation, Grammar-Correction, MWE, Multimodal, Misc). A new category needs user approval and a manually placed filter button (step 4).
   - `title`, `conference` — use `VENUE YEAR (to appear)` for accepted-but-unpublished papers, e.g. `WMT 2026 (to appear)`.
   - `authors`: comma-separated full names in paper order (the script also accepts `Last, First; ...`).
   - `pub_url`: arXiv abstract URL. `paper_type`: e.g. Full Paper, Short Paper, Shared Task, Tutorial, Workshop. Leave `author_pub_id`, `awards`, `notes` empty.
3. `cd scripts && python3 create_publication_list.py` → `my_publications.html`.
4. In `_pages/publications.html`, replace **only** the `<ol id='publicationList'>…</ol>` block. Do not touch the front matter, the Scholar note, or the "Filter by Research Area" buttons above it — their order is curated by hand.
5. Check the `<li class="publication-item` count on the page equals the number of sheet rows.

## Adding talks

1. Add rows to `scripts/my_talks.xlsx`: `talk_title`, `venue`, `date` (year), `collaborators` (optional), `slides`, `video`, `type`.
   - `type` must be exactly one of `Tutorial`, `Keynote`, `Invited Talk`, `Panel Discussion`, `Course Lecture` — any other value is silently dropped. A new type needs a change to `section_order` in `create_talks.py` and a new anchor link at the top of the talks page.
   - `slides` and `video`: either a full `http(s)` URL (used as is) or a path relative to `files/`, which the script prefixes with `/files/` (e.g. `publications/presentations/foo.pdf` → `/files/publications/presentations/foo.pdf`). Any non-`http` value gets the prefix, so never use a `/`-rooted path.
2. `cd scripts && python3 create_talks.py` → `my_talks.html`.
3. In `_pages/talks.html`, replace the block from `<h2 id="tutorials">` up to (not including) the commented-out `<!-- {% if site.talkmap_link` section. Keep the front matter, YouTube playlist link, and section anchor links.

## News items

- Announcements (paper acceptances, talks, releases) go in **both** `_pages/news.md` (under the current year's `<h2>`) and the News list in `_pages/about.md`, newest first, one `<li> <i>DD Mon YYYY</i>: ... </li>` line each.
- Paper style: `2 papers accepted at VENUE: <a href="arxiv-url"><i>Title</i></a> and ...`.
- `_pages/news.md` is CRLF and `_pages/about.md` is LF — preserve each.
