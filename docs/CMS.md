# إدارة محتوى الموقع — Website content management

> **بالعربية للمشرف على الموقع، وبالإنجليزية للمطوّر.** لا حاجة إلى معرفة بالبرمجة
> لتحديث الأخبار أو الفعاليات أو الصور.
>
> Arabic first for the web admin; the English summary for developers is at the end.

---

## ١. كيف يعمل الموقع بعد تفعيل لوحة التحكم

```
المشرف يعدّل المحتوى في Pages CMS
        ↓  (حفظ = commit في GitHub)
GitHub Actions يبني الموقع من content/**.json
        ↓
GitHub Pages ينشر النسخة الجديدة (خلال دقيقة إلى دقيقتين)
```

- المحتوى محفوظ في ملفات JSON داخل مجلد `content/` — لا توجد قاعدة بيانات.
- كل عملية حفظ تُسجَّل في تاريخ المستودع، فيمكن الرجوع عن أي تعديل.
- الموقع يبقى **مجانياً بالكامل**: استضافة GitHub Pages + لوحة تحكم Pages CMS المجانية.

**ما يمكن تعديله:** الأخبار، الفعاليات، الإعلانات، صور المعرض، نصوص كل صفحة، قائمة
التصفح، التذييل، وبيانات المساعد الذكي.

---

## ٢. الإعداد لأول مرة (مالك الموقع — مرة واحدة فقط)

1. **ارفع الملفات إلى GitHub**

   ```bash
   git add .
   git commit -m "feat(cms): content JSON + Pages CMS configuration"
   git push origin main
   ```

   يجب أن يكون الملف `.pages.yml` ومجلد `content/` على الفرع `main`، لأن اللوحة
   تقرأ إعداداتها من المستودع.

2. **افتح لوحة التحكم:** <https://app.pagescms.org> ثم **Sign in with GitHub**
   بحساب مالك المستودع (`engziada`).

3. **ثبّت تطبيق GitHub على المستودع:** اختر `engziada/AUEM` فقط (وليس كل
   المستودعات). هذه الخطوة تمنح اللوحة صلاحية الكتابة على هذا المستودع وحده.

4. **افتح المستودع** من قائمة اللوحة. ستظهر الأقسام العربية التالية في الشريط الجانبي:
   - الأخبار والفعاليات — Newsroom
   - صفحات الموقع — Website pages
   - إعدادات الموقع — Site settings
   - المساعد الذكي — Chatbot knowledge

5. **أضف المحررين (بدون حساب GitHub):**
   في اللوحة: إعدادات المستودع ← **Collaborators** ← أدخل بريد الموظف.
   يصله رابط دعوة، ينشئ كلمة مرور، ويبدأ التحرير. لا يحتاج إلى GitHub إطلاقاً.

6. **تحقّق من النشر:** عدّل كلمة في أي صفحة ثم احفظ. افتح تبويب **Actions** في
   GitHub وتأكد من نجاح العملية «Deploy AUEM Website to GitHub Pages».
   سيظهر التغيير على الموقع بعد دقيقة تقريباً.

> **ملاحظة:** واجهة لوحة التحكم بالإنجليزية، لكن **كل التسميات والحقول موصوفة
> بالعربية**، وأزرار الحفظ هي `Save`. إن رغبت في واجهة عربية بالكامل فهناك بديل
> (Sveltia أو Decap CMS) يحتاج استضافة إضافية — راجع نهاية الملف.

---

## ٣. المهام اليومية — أين أضغط؟

| المهمة | المسار في اللوحة |
| --- | --- |
| نشر خبر جديد | الأخبار والفعاليات ← **الأخبار — News articles** ← *Add entry* |
| إضافة فعالية | الأخبار والفعاليات ← **الفعاليات — Events** ← *Add entry* |
| إعلان يظهر في شريط أعلى الموقع | الأخبار والفعاليات ← **الإعلانات — Announcements** |
| رفع صور إلى المعرض | الأخبار والفعاليات ← **معرض الصور — Gallery photos** |
| تعديل نص صفحة (الرئيسية، عن الاتحاد…) | صفحات الموقع ← اختر الصفحة |
| تغيير اسم الاتحاد أو التذييل أو قائمة التصفح | **إعدادات الموقع — Site settings** |
| تعليم المساعد الذكي جواباً جديداً | **المساعد الذكي — Chatbot knowledge** |

### خبر جديد — الحقول

| الحقل | إلزامي | ملاحظات |
| --- | --- | --- |
| العنوان — Title | ✔ | عربي وإنجليزي |
| تاريخ النشر — Publication date | ✔ | يظهر بالتنسيق المحلي (٢٣ يوليو ٢٠٢٦) |
| ملخص قصير — Summary | — | يظهر في الصفحة الرئيسية؛ إن تُرك فارغاً يُقتطع من النص |
| نص الخبر — Body | — | فقرة واحدة في كل سطر |
| صورة الخبر — Image | — | تظهر بجانب الخبر وتُصغَّر تلقائياً |
| المصدر / الرابط — Source | — | يظهر كوسم أسفل الخبر |
| منشور — Published | — | أطفئه لإخفاء الخبر دون حذفه |

### فعالية جديدة

- **تاريخ البداية** يحدّد تلقائياً إن كانت الفعالية «قادمة» أو «سابقة» على صفحة
  الفعاليات، وتظهر القادمة منها في الصفحة الرئيسية.
- **رابط التسجيل** يضيف زر «التسجيل».
- **تاريخ النهاية** اختياري، ويُعرض كمدى زمني.

### إعلان في الشريط العلوي

- يُعرض فقط عند تفعيل **مفعّل — Active**.
- **مستوى الأهمية:** `مهم` يبرز النص بالذهبي.
- **ينتهي في** يخفي الإعلان تلقائياً بعد التاريخ المحدد (مفيد للإعلانات المؤقتة).
- الزائر يستطيع إغلاق الشريط، ولا يعود يظهر له (يُحفظ في متصفحه).

### صور المعرض

- أضف صورة + تعليقاً بالعربية والإنجليزية + التاريخ.
- أحدث الصور تظهر أولاً في صفحة المعرض، وتظهر آخر ست صور في الصفحة الرئيسية.
- النقر على صورة يفتحها بالحجم الكامل (lightbox).

### تعديل نصوص الصفحات

كل صفحة ملف مستقل. الحقول مقسومة دائماً إلى **العربية** و**English**:

- **نص** = سطر واحد.
- **نص طويل** = فقرة في كل سطر (كل سطر يظهر كفقرة منفصلة).
- في القوائم (مثل الأهداف والمرتكزات) أضف عنصراً لكل بند.

---

## ٤. الصور — أفضل الممارسات

- الصيغ المقبولة: `jpg` / `png` / `webp` — **JPEG للصور الفوتوغرافية**.
- العرض الموصى به: **1600 بكسل** كحد أقصى، وأقل من **2 ميغابايت** قبل الرفع.
- الصور تُحسَّن تلقائياً عند البناء:
  - نسخة كاملة حتى 2000 بكسل،
  - نسخة مصغّرة 760 بكسل للبطاقات والشبكات،
  - شعارات الموقع تُحوَّل إلى WebP (من 2.8 ميغابايت إلى ~34 كيلوبايت).
- تُحفظ الملفات في `assets/img/uploads/<القسم>/` وتُعاد تسميتها تلقائياً بأسماء
  لاتينية آمنة — التعليق العربي هو ما يُعرض للزائر.
- عند اختيار صورة موجودة مسبقاً استخدم زر **Browse** بدل رفعها مرة أخرى.

---

## ٥. المسودات والرجوع عن التعديل

- **منشور / Published = false** يخفي الخبر أو الفعالية أو الصورة دون حذفها.
- **الإعلانات** لا تظهر إلا عند تفعيلها.
- كل حفظ = عملية `commit` باسم واضح في GitHub. للرجوع: افتح المستودع ←
  **Commits** ← اختر الحفظ السابق ← **Revert** (أو اسأل المطوّر).
- لا حذف نهائي: الملفات تبقى في تاريخ المستودع.

---

## ٦. اللغتان العربية والإنجليزية

- كل نص مخزَّن كزوج `{"ar": "...", "en": "..."}`.
- إذا تُرجم أحد الحقلين وفُرغ الآخر، **يُعرض النص الموجود في اللغتين** بدل ترك
  فراغ — فلا تتعطّل الصفحة أبداً بسبب ترجمة ناقصة.
- الصفحات تُبنى دائماً بالنسختين: `/ar/…` و `/en/…`.

---

## ٧. خريطة الملفات (للمطوّر)

```
content/
  settings.json        اسم الاتحاد، الشعار، المقر، البريد، قائمة التصفح، التذييل
  pages/
    index.json about.json objectives.json governance.json membership.json
    activities.json news.json events.json gallery.json unions.json contact.json
  news/*.json          خبر واحد لكل ملف        (collection)
  events/*.json        فعالية واحدة لكل ملف    (collection)
  announcements/*.json إعلان واحد لكل ملف      (collection)
  gallery/*.json       صورة واحدة لكل ملف      (collection)
  chatbot.json         نصوص المساعد + قاعدة المعرفة
.pages.yml             مخطط لوحة التحكم (ما يظهر للمشرف وأين يُخزَّن)
build.py               يقرأ content/**/*.json ويبني dist/
tools/check_content.py يتحقق من تطابق .pages.yml مع ملفات JSON
tools/check_site.py    يتحقق من الروابط والصور في dist/
tools/migrate_content.py  هجرة المحتوى القديم (مرة واحدة، موثّقة في تاريخ git)
assets/img/uploads/    الملفات المرفوعة من اللوحة
```

`build.py` لا يحتوي أي نص من الموقع — كل النصوص من `content/`.

---

## ٨. البناء والتحقق محلياً

```bash
python build.py                     # يبني dist/
python build.py --out .preview      # بناء في مجلد آخر دون لمس dist/
python tools/check_content.py       # تطابق الإعدادات مع المحتوى
python tools/check_site.py .preview # روابط وصور مكسورة
python -m http.server 8000 --directory .preview
```

> يتطلب `tools/check_content.py` حزمة `pyyaml`، ويستخدم `build.py` حزمة `Pillow`
> عند توفرها لتحسين الصور (وإلا ينسخ الصور كما هي).

---

## ٩. استكشاف الأخطاء

| العَرَض | السبب المحتمل | الحل |
| --- | --- | --- |
| حفظت ولم يتغيّر الموقع | فشل GitHub Actions | تبويب **Actions** ← آخر عملية ← اقرأ الخطأ |
| الموقع ما زال يعرض النسخة القديمة | ذاكرة المتصفح | تحديث قوي: `Ctrl + F5` |
| صورة لا تظهر | مسار خاطئ أو ملف محذوف | افتح الصورة من المعرض وأعد رفعها، ثم `check_site.py` |
| خطأ في البناء «invalid JSON» | تعديل يدوي لملف JSON | أعد التعديل من اللوحة، أو استرجع الملف من تاريخ git |
| الشريط الجانبي في اللوحة فارغ | `.pages.yml` غير موجود على `main` | ادمج الفرع ثم أعد فتح اللوحة |
| الإعلان لا يظهر | `Active` مطفأ أو التاريخ منتهٍ | فعّله وتأكد من تاريخ «ينتهي في» |
| الفعالية في «قادمة» بعد انتهائها | الموقع يُبنى عند كل تعديل فقط | يعيد البناء المجدول يومياً تصحيح ذلك تلقائياً |

---

## 10. English summary (developers)

- **CMS:** [Pages CMS](https://app.pagescms.org) — free, git-based, config-only.
  Editors are invited by email and never need a GitHub account; every save is a
  commit, which triggers the existing GitHub Pages workflow.
- **Single source of truth:** `content/**/*.json`. `build.py` holds no copy.
  `content.py` is retired (stub) and kept only for history.
- **Schema:** `.pages.yml` (media sources, reusable bilingual components, page
  files, four collections). Keep field names identical to JSON keys and run
  `python tools/check_content.py` — it fails on drift, on unknown keys (which
  the CMS would silently drop), on bad dates/selects and on missing images.
- **Rendering:** gallery, events and announcements are new; news/events dates are
  localised (`٢٣ يوليو ٢٠٢٦` / `23 July 2026`); empty collections render a styled
  empty state instead of breaking.
- **Media:** uploads land in `assets/img/uploads/<section>/` and are optimised at
  build time (max 2000 px, 760 px thumbnails in `uploads/thumbs/`, WebP brand
  marks). Pillow is optional — without it images are copied untouched.
- **Checks in CI:** `check_content.py` → `build.py` → `check_site.py` (broken
  links, missing assets, missing pages). A daily cron rebuild keeps
  upcoming/past event classification fresh.
- **Trade-off:** the Pages CMS chrome is English-only, hence Arabic labels on
  every collection, field and hint. If a fully Arabic UI ever becomes a
  requirement, the same `content/` + `build.py` work with Sveltia or Decap CMS
  behind a Netlify or Cloudflare OAuth helper — only `.pages.yml` would be
  replaced by `admin/config.yml`.
