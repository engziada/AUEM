# Gallery photos

Each `.json` file in this folder is one photo in the gallery.

Add photos from the CMS (**معرض الصور — Gallery photos** → *Add entry*), not by hand.
The file is excluded from the CMS list.

Fields:

| key         | meaning                                              |
| ----------- | ---------------------------------------------------- |
| `image`     | path such as `/assets/img/uploads/gallery/<file>.jpg` |
| `caption`   | `{ "ar": "...", "en": "..." }` — shows on hover      |
| `date`      | `YYYY-MM-DD` — newest first everywhere               |
| `published` | `false` hides the photo without deleting it          |
