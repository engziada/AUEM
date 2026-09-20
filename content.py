# -*- coding: utf-8 -*-
"""All bilingual (AR/EN) content for the AUEM website.
Sourced from press coverage of the founding General Assembly (Salé, 23 July 2026)
and the League of Arab States / Council of Arab Economic Unity ecosystem.
"""

SITE = {
    "name": {"ar": "الاتحاد العربي للطاقة والمعادن", "en": "Arab Union for Energy & Minerals"},
    "abbr": "AUEM",
    "tagline": {
        "ar": "المنصة العربية المرجعية للطاقة والمعادن",
        "en": "The pan-Arab reference platform for energy and minerals",
    },
    "hq": {"ar": "الدار البيضاء، المملكة المغربية", "en": "Casablanca, Kingdom of Morocco"},
}

NAV = [
    ("index",       {"ar": "الرئيسية",      "en": "Home"}),
    ("about",       {"ar": "عن الاتحاد",     "en": "About"}),
    ("objectives",  {"ar": "الأهداف",        "en": "Objectives"}),
    ("governance",  {"ar": "الهيكل التنظيمي", "en": "Governance"}),
    ("membership",  {"ar": "العضوية",        "en": "Membership"}),
    ("activities",  {"ar": "الأنشطة",        "en": "Activities"}),
    ("news",        {"ar": "الأخبار",        "en": "News"}),
    ("unions",      {"ar": "اتحادات عربية",  "en": "Arab Unions"}),
    ("contact",     {"ar": "اتصل بنا",       "en": "Contact"}),
]

PAGES = {
    # ------------------------------------------------------------------ HOME
    "index": {
        "title": {"ar": "الرئيسية", "en": "Home"},
        "meta": {
            "ar": "الاتحاد العربي للطاقة والمعادن — منصة مؤسسية لتعزيز العمل العربي المشترك في قطاعي الطاقة والمعادن. المقر: الدار البيضاء، المغرب.",
            "en": "The Arab Union for Energy & Minerals — an institutional platform advancing joint Arab action in the energy and minerals sectors. Headquarters: Casablanca, Morocco.",
        },
        "hero_kicker": {
            "ar": "تأسس في 23 يوليو 2026 — سلا، المملكة المغربية",
            "en": "Founded 23 July 2026 — Salé, Kingdom of Morocco",
        },
        "hero_sub": {
            "ar": "منصة مؤسسية جديدة تهدف إلى دفع دينامية جديدة للعمل العربي المشترك في قطاعي الطاقة والمعادن، وتحويل الموارد الطاقية والمعدنية في العالم العربي إلى مشاريع مهيكلة وشراكات استراتيجية وفرص استثمارية ملموسة.",
            "en": "A new institutional platform driving joint Arab action across the energy and minerals sectors, turning the Arab world's energy and mineral resources into structured projects, strategic partnerships and concrete investment opportunities.",
        },
        "cta_primary": {"ar": "تعرف على الاتحاد", "en": "Discover the Union"},
        "cta_secondary": {"ar": "انضم إلينا", "en": "Become a member"},
        "stats_title": {"ar": "الاتحاد في لمحة", "en": "The Union at a glance"},
        "stats": [
            ({"ar": "23 يوليو 2026", "en": "23 July 2026"},
             {"ar": "الجمعية العمومية التأسيسية بمدينة سلا المغربية", "en": "Inaugural General Assembly held in Salé, Morocco"}),
            ({"ar": "الدار البيضاء", "en": "Casablanca"},
             {"ar": "المقر الرئيسي للاتحاد", "en": "Headquarters of the Union"}),
            ({"ar": "المغرب", "en": "Morocco"},
             {"ar": "انتخب بالإجماع لرئاسة الاتحاد", "en": "Unanimously elected to the presidency"}),
            ({"ar": "8 لجان متخصصة", "en": "8 specialized commissions"},
             {"ar": "تغطي الطاقة والنفط والغاز والمعادن والطاقات المتجددة والاستثمار والابتكار والعلاقات الدولية", "en": "Covering energy, oil, gas, minerals, renewables, investment, innovation and international relations"}),
        ],
        "sectors_title": {"ar": "القطاعات التي نعمل فيها", "en": "Sectors we serve"},
        "sectors_sub": {
            "ar": "يعمل الاتحاد على توحيد الرؤى وتنسيق خطط العمل بين الفاعلين في قطاعي الطاقة والمعادن في الدول العربية.",
            "en": "The Union unifies visions and coordinates action plans among stakeholders in the Arab energy and minerals sectors.",
        },
        "sectors": [
            {"icon": "oil",
             "name": {"ar": "النفط والغاز", "en": "Oil & Gas"},
             "desc": {"ar": "تنسيق الرؤى وخطط العمل بين الفاعلين في قطاع النفط والغاز في ظل تقلبات الأسواق العالمية.", "en": "Coordinating visions and action plans among oil and gas stakeholders amid global market volatility."}},
            {"icon": "mining",
             "name": {"ar": "المعادن والتعدين", "en": "Minerals & Mining"},
             "desc": {"ar": "تطوير قطاع تعديني عربي يتماشى مع أفضل الممارسات الدولية ويعزز السيادة الصناعية.", "en": "Developing an Arab mining sector aligned with international best practices and industrial sovereignty."}},
            {"icon": "renewable",
             "name": {"ar": "الطاقات المتجددة", "en": "Renewable Energy"},
             "desc": {"ar": "مواكبة الانتقال الطاقي عبر دعم مشاريع الطاقة المتجددة والهيدروجين الأخضر وكفاءة الطاقة.", "en": "Supporting the energy transition through renewables, green hydrogen and energy-efficiency projects."}},
            {"icon": "invest",
             "name": {"ar": "الاستثمار والشراكات", "en": "Investment & Partnerships"},
             "desc": {"ar": "تشجيع الاستثمارات العربية والدولية وتثمين الفرص الكامنة في دول المنطقة.", "en": "Promoting Arab and international investment and valorizing opportunities across the region."}},
        ],
        "about_teaser_title": {"ar": "من نحن", "en": "Who we are"},
        "about_teaser": {
            "ar": "الاتحاد العربي للطاقة والمعادن منظمة مهنية عربية أُعلن عن تأسيسها خلال جمعيتها العمومية التأسيسية المنعقدة بمدينة سلا بالمملكة المغربية في 23 يوليو 2026، وانتخب المغرب بالإجماع لرئاستها، ويستضيف مقرها في الدار البيضاء. يطمح الاتحاد إلى أن يصبح المنصة العربية المرجعية التي تجعل من الطاقة والمعادن روافع للتنمية المستدامة والتكامل الاقتصادي الإقليمي.",
            "en": "The Arab Union for Energy & Minerals is a pan-Arab professional organization whose establishment was announced at its inaugural General Assembly in Salé, Kingdom of Morocco, on 23 July 2026. Morocco was unanimously elected to its presidency, and its headquarters is hosted in Casablanca. The Union aspires to become the Arab reference platform making energy and minerals levers of sustainable development and regional economic integration.",
        },
        "about_more": {"ar": "اقرأ المزيد عن الاتحاد", "en": "Read more about the Union"},
        "news_title": {"ar": "آخر الأخبار", "en": "Latest news"},
        "news_more": {"ar": "جميع الأخبار", "en": "All news"},
        "partners_title": {"ar": "شراكات مرتقبة", "en": "Envisioned partnerships"},
        "partners_sub": {
            "ar": "يعمل الاتحاد على بناء شراكات مع مؤسسات عربية وإقليمية ودولية، وشركات الطاقة والتعدين ومراكز البحث والجامعات.",
            "en": "The Union is building partnerships with Arab, regional and international institutions, energy and mining companies, research centers and universities.",
        },
        "partners": [
            {"ar": "جامعة الدول العربية", "en": "League of Arab States"},
            {"ar": "مجلس الوحدة الاقتصادية العربية", "en": "Council of Arab Economic Unity"},
            {"ar": "المنظمة العربية للتنمية الصناعية والتقييس والتعدين", "en": "Arab Industrial Development, Standardization & Mining Organization"},
            {"ar": "البنك الإسلامي للتنمية", "en": "Islamic Development Bank"},
            {"ar": "البنك الإفريقي للتنمية", "en": "African Development Bank"},
            {"ar": "الاتحاد الإفريقي", "en": "African Union"},
        ],
        "join_title": {"ar": "كن جزءاً من العمل العربي المشترك", "en": "Be part of joint Arab action"},
        "join_sub": {
            "ar": "يضم الاتحاد فاعلين اقتصاديين ومؤسسات وشركات وخبراء من القطاع الخاص في الدول العربية في قطاعي الطاقة والمعادن.",
            "en": "The Union brings together economic actors, institutions, companies and experts from the private sector of Arab countries in the energy and minerals sectors.",
        },
        "join_cta": {"ar": "طلب العضوية", "en": "Request membership"},
    },

    # ------------------------------------------------------------------ ABOUT
    "about": {
        "title": {"ar": "عن الاتحاد", "en": "About the Union"},
        "meta": {
            "ar": "تعرف على نشأة الاتحاد العربي للطاقة والمعادن ورؤيته ورسالته وقصة تأسيسه في المغرب.",
            "en": "Learn about the establishment, vision and mission of the Arab Union for Energy & Minerals.",
        },
        "intro_title": {"ar": "نشأة الاتحاد", "en": "Establishment"},
        "intro": {
            "ar": """انعقدت يوم الخميس 23 يوليو 2026 بمدينة سلا بالمملكة المغربية الجمعية العمومية التأسيسية للاتحاد العربي للطاقة والمعادن، مما مثّل الإطلاق الرسمي لهذه المنصة المؤسسية الجديدة التي تهدف إلى دفع دينامية جديدة للعمل العربي المشترك في هذين القطاعين الاستراتيجيين.

وقد جمع اللقاء التأسيسي صنّاع قرار ومسؤولين وخبراء وفاعلين اقتصاديين يمثلون القطاع الخاص من عدة دول عربية، وانتُخب المغرب بالإجماع لرئاسة هذه المنظمة الجديدة التي يقع مقرها في الدار البيضاء.

وجاء تأسيس الاتحاد بمبادرة من شركة «يونايتد بتروليوم» بصفتها العضو المؤسس والشريك الاستراتيجي، وهو ثمرة مشاورات ولقاءات عديدة بين الشركاء العرب توّجت بالتوافق على اختيار المغرب لاحتضان المنظمة. وخلال الجمعية تم الكشف عن اللجنة التأسيسية والبرنامج السنوي وخارطة الطريق للفترة 2026–2030.""",
            "en": """The inaugural General Assembly of the Arab Union for Energy & Minerals was held on Thursday, 23 July 2026, in Salé, Kingdom of Morocco — the official launch of a new institutional platform aimed at driving joint Arab action in these two strategic sectors.

The founding meeting brought together decision-makers, officials, experts and economic actors representing the private sector of several Arab countries. Morocco was unanimously elected to the presidency of the new organization, whose headquarters is located in Casablanca.

The Union was established on the initiative of United Petroleum as founding member and strategic partner, and is the fruit of extensive consultations among Arab partners that concluded with a consensus on Morocco as host. The Assembly unveiled the founding committee, the annual programme, and the 2026–2030 roadmap.""",
        },
        "vision_title": {"ar": "الرؤية", "en": "Vision"},
        "vision": {
            "ar": "أن يصبح الاتحاد المنصة العربية المرجعية الرئيسية التي تجعل من الطاقة والمعادن روافع للتنمية المستدامة والتكامل الاقتصادي الإقليمي.",
            "en": "To become the leading pan-Arab reference platform making energy and minerals levers of sustainable development and regional economic integration.",
        },
        "mission_title": {"ar": "الرسالة", "en": "Mission"},
        "mission": {
            "ar": "تعزيز موقع الدول العربية في الساحة الدولية في قطاعي الصناعات الطاقية والتعدينية، من خلال تطوير شراكات استراتيجية بين الحكومات والمؤسسات والشركات والمستثمرين ومراكز البحث والجامعات.",
            "en": "Strengthening the position of Arab countries on the international stage in the energy and mining industries by developing strategic partnerships among governments, institutions, companies, investors, research centers and universities.",
        },
        "context_title": {"ar": "السياق الاستراتيجي", "en": "Strategic context"},
        "context": {
            "ar": "يأتي إنشاء الاتحاد في سياق عالمي يتسم بتحولات استراتيجية كبرى، حيث أصبحت الطاقة والموارد المعدنية تحتل مكانة مركزية في رهانات الأمن الاقتصادي والسيادة الصناعية والانتقال الطاقي. وفي ظل تقلبات الأسواق العالمية، لا سيما أسعار النفط، يشكّل إنشاء هذا التجمع المهني أمراً بالغ الأهمية لتوحيد الرؤى وتنسيق خطط العمل العربية.",
            "en": "The Union's creation comes in a global context marked by major strategic shifts, in which energy and mineral resources now occupy a central place in economic security, industrial sovereignty and energy transition. Amid the volatility of global markets — particularly oil prices — establishing this professional grouping is of paramount importance to unify visions and coordinate Arab action plans.",
        },
        "pillars_title": {"ar": "الركائز التأسيسية", "en": "Founding pillars"},
        "pillars": [
            {"ar": "دمج التكنولوجيات الجديدة في قطاعي الطاقة والمعادن", "en": "Integrating new technologies into the energy and minerals sectors"},
            {"ar": "تعزيز البحث العلمي والطاقات النظيفة", "en": "Promoting scientific research and clean energy"},
            {"ar": "خفض الانبعاثات تماشياً مع أهداف التنمية المستدامة", "en": "Reducing emissions in line with the Sustainable Development Goals"},
            {"ar": "توحيد الجهود العربية لرفع التحديات العالمية المتسارعة", "en": "Unifying Arab efforts to meet accelerating global challenges"},
        ],
        "president_title": {"ar": "كلمة الرئيس", "en": "From the President"},
        "president_name": {"ar": "صلاح الدين البدري", "en": "Salah Eddine El Badry"},
        "president_role": {"ar": "رئيس الاتحاد العربي للطاقة والمعادن", "en": "President of the Arab Union for Energy & Minerals"},
        "president_quote": {
            "ar": "«إنشاء هذا التجمع المهني أمر بالغ الأهمية من أجل توحيد الرؤى وتنسيق خطط العمل، وهو ثمرة مشاورات ولقاءات عديدة توّجت بالتوافق على اختيار المغرب لاحتضان هذه المنظمة العربية الهامة.»",
            "en": "“Establishing this professional grouping is of paramount importance for unifying visions and coordinating action plans. It is the fruit of extensive consultations that concluded with a consensus on Morocco as host of this important Arab organization.”",
        },
        "timeline_title": {"ar": "محطات رئيسية", "en": "Key milestones"},
        "timeline": [
            ("2026-07-23",
             {"ar": "انعقاد الجمعية العمومية التأسيسية في سلا وانتخاب المغرب رئيساً للاتحاد", "en": "Inaugural General Assembly in Salé; Morocco unanimously elected to the presidency"}),
            ("2026-07-23",
             {"ar": "ندوة صحفية للجنة التأسيسية: الإعلان عن اللجنة التأسيسية والبرنامج السنوي وخارطة الطريق 2026–2030", "en": "Founding committee press conference: founding committee, annual programme and 2026–2030 roadmap unveiled"}),
            ("2026",
             {"ar": "انطلاق الأعمال التحضيرية لاستكمال الأجهزة واللجان المتخصصة وتفعيل الشراكات", "en": "Preparatory work begins to complete governance bodies, specialized commissions and partnerships"}),
        ],
    },

    # --------------------------------------------------------------- OBJECTIVES
    "objectives": {
        "title": {"ar": "الأهداف الاستراتيجية", "en": "Strategic Objectives"},
        "meta": {
            "ar": "الأهداف الاستراتيجية للاتحاد العربي للطاقة والمعادن: التكامل العربي، الاستثمار، الأمن الطاقي، الانتقال الطاقي، تطوير التعدين.",
            "en": "The strategic objectives of the Arab Union for Energy & Minerals: Arab integration, investment, energy security, energy transition and mining development.",
        },
        "intro": {
            "ar": "حدّدت الجمعية العمومية التأسيسية للاتحاد مجموعة من الأهداف الاستراتيجية التي تؤطر عمله في خدمة التكامل الاقتصادي العربي في قطاعي الطاقة والمعادن:",
            "en": "The Union's inaugural General Assembly defined a set of strategic objectives that frame its work in service of Arab economic integration in the energy and minerals sectors:",
        },
        "items": [
            {"ar": "تعزيز التكامل العربي من خلال تطوير شبكة تعاون بين الحكومات والمؤسسات والشركات العاملة في قطاعي الطاقة والمعادن.",
             "en": "Strengthen Arab integration by developing a cooperation network among governments, institutions and companies operating in the energy and minerals sectors."},
            {"ar": "تشجيع الاستثمارات العربية والدولية وتثمين الفرص الكامنة في دول المنطقة.",
             "en": "Encourage Arab and international investment and valorize the region's inherent opportunities."},
            {"ar": "المساهمة في تعزيز الأمن الطاقي العربي والتدبير المستدام للموارد الطبيعية.",
             "en": "Contribute to strengthening Arab energy security and the sustainable management of natural resources."},
            {"ar": "مواكبة الانتقال الطاقي عبر دعم مشاريع الطاقة المتجددة والهيدروجين الأخضر وكفاءة الطاقة.",
             "en": "Accompany the energy transition by supporting renewable-energy, green-hydrogen and energy-efficiency projects."},
            {"ar": "تشجيع تطوير قطاع تعديني يتماشى مع أفضل الممارسات الدولية.",
             "en": "Promote the development of a mining sector aligned with international best practices."},
            {"ar": "تحفيز البحث العلمي والابتكار ونقل التكنولوجيا ودمج التكنولوجيات الجديدة.",
             "en": "Stimulate scientific research, innovation, technology transfer and the integration of new technologies."},
            {"ar": "تعزيز الدبلوماسية الاقتصادية العربية وموقع الدول العربية في الصناعات الطاقية والتعدينية دولياً.",
             "en": "Advance Arab economic diplomacy and the international standing of Arab countries in the energy and mining industries."},
            {"ar": "خفض الانبعاثات ودعم الطاقات النظيفة تماشياً مع أهداف التنمية المستدامة.",
             "en": "Reduce emissions and support clean energy in line with the Sustainable Development Goals."},
        ],
    },

    # --------------------------------------------------------------- GOVERNANCE
    "governance": {
        "title": {"ar": "الهيكل التنظيمي", "en": "Governance"},
        "meta": {
            "ar": "الهيكل التنظيمي والحكامة في الاتحاد العربي للطاقة والمعادن: المجلس الأعلى، مجلس الإدارة، الأمانة العامة، المجلس الاستشاري الدولي واللجان المتخصصة.",
            "en": "Governance of the Arab Union for Energy & Minerals: Superior Council, Board of Directors, General Secretariat, International Advisory Council and specialized commissions.",
        },
        "intro": {
            "ar": "يعتمد الاتحاد حكامة متكاملة تضم مجلساً أعلى ومجلس إدارة وأمانة عامة ومجلساً استشارياً دولياً، بالإضافة إلى لجان متخصصة تغطي مجالات عمله.",
            "en": "The Union relies on an integrated governance structure comprising a Superior Council, a Board of Directors, a General Secretariat, an International Advisory Council and specialized commissions covering its fields of work.",
        },
        "bodies_title": {"ar": "أجهزة الاتحاد", "en": "Organs of the Union"},
        "bodies": [
            {"name": {"ar": "المجلس الأعلى", "en": "Superior Council"},
             "desc": {"ar": "أعلى هيئة توجيهية في الاتحاد، تحدد التوجهات الاستراتيجية العامة.", "en": "The Union's highest steering body; sets overall strategic directions."}},
            {"name": {"ar": "مجلس الإدارة", "en": "Board of Directors"},
             "desc": {"ar": "يشرف على تنفيذ الاستراتيجيات وإدارة أعمال الاتحاد بين الدورات.", "en": "Oversees implementation of strategies and the Union's business between sessions."}},
            {"name": {"ar": "الأمانة العامة", "en": "General Secretariat"},
             "desc": {"ar": "الجهاز التنفيذي اليومي للاتحاد، تتولى التنسيق والمتابعة والتواصل.", "en": "The Union's day-to-day executive arm, responsible for coordination, follow-up and communication."}},
            {"name": {"ar": "المجلس الاستشاري الدولي", "en": "International Advisory Council"},
             "desc": {"ar": "يقدم الخبرة والمشورة الدولية لدعم قرارات الاتحاد وشراكاته.", "en": "Provides international expertise and advice supporting the Union's decisions and partnerships."}},
        ],
        "commissions_title": {"ar": "اللجان المتخصصة", "en": "Specialized commissions"},
        "commissions_sub": {
            "ar": "تغطي اللجان المتخصصة مجالات العمل القطاعية والموضوعية للاتحاد:",
            "en": "Specialized commissions cover the Union's sectoral and thematic fields of work:",
        },
        "commissions": [
            {"ar": "الطاقة", "en": "Energy"},
            {"ar": "النفط", "en": "Oil"},
            {"ar": "الغاز", "en": "Gas"},
            {"ar": "المعادن والتعدين", "en": "Minerals & Mining"},
            {"ar": "الطاقات المتجددة", "en": "Renewable Energies"},
            {"ar": "الاستثمار", "en": "Investment"},
            {"ar": "الابتكار وريادة الأعمال", "en": "Innovation & Entrepreneurship"},
            {"ar": "العلاقات الدولية", "en": "International Relations"},
        ],
        "leadership_title": {"ar": "القيادة", "en": "Leadership"},
        "leaders": [
            {"name": {"ar": "المملكة المغربية", "en": "Kingdom of Morocco"},
             "role": {"ar": "رئاسة الاتحاد — انتخبت بالإجماع في الجمعية العمومية التأسيسية", "en": "Presidency of the Union — unanimously elected at the inaugural General Assembly"}},
            {"name": {"ar": "صلاح الدين البدري", "en": "Salah Eddine El Badry"},
             "role": {"ar": "رئيس الاتحاد العربي للطاقة والمعادن", "en": "President of the Arab Union for Energy & Minerals"}},
            {"name": {"ar": "إسماعيل الجنابي", "en": "Ismaeil Al Janaby"},
             "role": {"ar": "عضو مؤسس بمجلس إدارة الاتحاد", "en": "Founding member of the Union's Board of Directors"}},
            {"name": {"ar": "شركة يونايتد بتروليوم", "en": "United Petroleum"},
             "role": {"ar": "العضو المؤسس والشريك الاستراتيجي", "en": "Founding member and strategic partner"}},
        ],
    },

    # --------------------------------------------------------------- MEMBERSHIP
    "membership": {
        "title": {"ar": "العضوية", "en": "Membership"},
        "meta": {
            "ar": "عضوية الاتحاد العربي للطاقة والمعادن مفتوحة للفاعلين الاقتصاديين والمؤسسات والشركات والخبراء في قطاعي الطاقة والمعادن بالدول العربية.",
            "en": "Membership of the Arab Union for Energy & Minerals is open to economic actors, institutions, companies and experts in the energy and minerals sectors across Arab countries.",
        },
        "intro_title": {"ar": "من يمكنه الانضمام؟", "en": "Who can join?"},
        "intro": {
            "ar": "يضم الاتحاد فاعلين اقتصاديين يمثلون القطاع الخاص في الدول العربية بقطاعي الطاقة والمعادن: شركات الطاقة والنفط والغاز والتعدين، والمؤسسات، والمستثمرين، ومراكز البحث، والجامعات، والخبراء والمختصين.",
            "en": "The Union brings together economic actors representing the private sector of Arab countries in the energy and minerals sectors: energy, oil, gas and mining companies, institutions, investors, research centers, universities, experts and specialists.",
        },
        "benefits_title": {"ar": "لماذا الانضمام؟", "en": "Why join?"},
        "benefits": [
            {"ar": "الانخراط في شبكة تعاون عربية تجمع الحكومات والمؤسسات والشركات العاملة في القطاعين.", "en": "Join an Arab cooperation network bringing together governments, institutions and companies in both sectors."},
            {"ar": "الوصول إلى فرص الاستثمار والشراكات الاستراتيجية التي يوفرها الاتحاد.", "en": "Access investment opportunities and strategic partnerships facilitated by the Union."},
            {"ar": "المساهمة في صياغة الرؤى وخطط العمل العربية المشتركة في الطاقة والمعادن.", "en": "Contribute to shaping common Arab visions and action plans for energy and minerals."},
            {"ar": "المشاركة في اللجان المتخصصة والفعاليات والبرامج التدريبية والبحثية.", "en": "Take part in specialized commissions, events, and training and research programmes."},
            {"ar": "تعزيز الحضور الدولي عبر منصة تمثّل الصناعات الطاقية والتعدينية العربية.", "en": "Strengthen international presence through a platform representing Arab energy and mining industries."},
        ],
        "how_title": {"ar": "كيفية الانضمام", "en": "How to join"},
        "how": {
            "ar": "للراغبين في الانضمام إلى الاتحاد، يرجى التواصل مع الأمانة العامة عبر صفحة «اتصل بنا» مع ذكر اسم الجهة ومجال عملها والدولة. وسيقوم فريق الاتحاد بمشاركة وثائق وشروط العضوية فور اعتمادها رسمياً ضمن خارطة الطريق 2026–2030.",
            "en": "To join the Union, please contact the General Secretariat via the Contact page, indicating your organisation's name, field of activity and country. The Union's team will share membership documentation and criteria once officially adopted under the 2026–2030 roadmap.",
        },
        "note": {
            "ar": "ملاحظة: إطار العضوية ورسومها يجري استكمالها من قبل الأجهزة المختصة في الاتحاد وفق خارطة الطريق المعتمدة.",
            "en": "Note: the membership framework and fees are being finalized by the Union's competent bodies under the adopted roadmap.",
        },
        "cta": {"ar": "تواصل معنا للعضوية", "en": "Contact us about membership"},
    },

    # --------------------------------------------------------------- ACTIVITIES
    "activities": {
        "title": {"ar": "الأنشطة ومجالات العمل", "en": "Activities & Workstreams"},
        "meta": {
            "ar": "مجالات عمل الاتحاد العربي للطاقة والمعادن: التكامل العربي، الاستثمار، الانتقال الطاقي، تطوير التعدين، البحث والابتكار، الدبلوماسية الاقتصادية.",
            "en": "Workstreams of the Arab Union for Energy & Minerals: Arab integration, investment, energy transition, mining development, research & innovation, economic diplomacy.",
        },
        "intro": {
            "ar": "يعمل الاتحاد على تحويل الموارد الطاقية والمعدنية الهامة في العالم العربي إلى مشاريع مهيكلة وشراكات استراتيجية وفرص استثمارية ملموسة، عبر مجالات عمل متكاملة:",
            "en": "The Union works to transform the Arab world's significant energy and mineral resources into structured projects, strategic partnerships and concrete investment opportunities through integrated workstreams:",
        },
        "streams": [
            {"name": {"ar": "التكامل والربط العربي", "en": "Arab integration & networking"},
             "desc": {"ar": "تطوير شبكة تعاون بين الحكومات والمؤسسات والشركات العاملة في قطاعي الطاقة والمعادن لتوحيد الرؤى وتنسيق خطط العمل.", "en": "Developing a cooperation network among governments, institutions and companies in the energy and minerals sectors to unify visions and coordinate action plans."}},
            {"name": {"ar": "تشجيع الاستثمار", "en": "Investment promotion"},
             "desc": {"ar": "تشجيع الاستثمارات العربية والدولية وتثمين الفرص الكامنة في دول المنطقة وتحويلها إلى مشاريع ملموسة.", "en": "Encouraging Arab and international investment and valorizing the region's opportunities into concrete projects."}},
            {"name": {"ar": "الانتقال الطاقي", "en": "Energy transition"},
             "desc": {"ar": "دعم مشاريع الطاقة المتجددة والهيدروجين الأخضر وكفاءة الطاقة والطاقات النظيفة وخفض الانبعاثات.", "en": "Supporting renewable-energy, green-hydrogen, energy-efficiency and clean-energy projects and emissions reduction."}},
            {"name": {"ar": "تطوير قطاع التعدين", "en": "Mining sector development"},
             "desc": {"ar": "العمل على تطوير قطاع تعديني عربي يتماشى مع أفضل الممارسات الدولية ويعزز التدبير المستدام للموارد.", "en": "Developing an Arab mining sector aligned with international best practices and sustainable resource management."}},
            {"name": {"ar": "البحث والابتكار ونقل التكنولوجيا", "en": "Research, innovation & technology transfer"},
             "desc": {"ar": "تحفيز البحث العلمي ودمج التكنولوجيات الجديدة ودعم الابتكار وريادة الأعمال في القطاعين.", "en": "Stimulating scientific research, integrating new technologies, and supporting innovation and entrepreneurship in both sectors."}},
            {"name": {"ar": "الدبلوماسية الاقتصادية والشراكات الدولية", "en": "Economic diplomacy & international partnerships"},
             "desc": {"ar": "بناء شراكات مع المؤسسات العربية والإقليمية والدولية لتعزيز موقع الدول العربية في الصناعات الطاقية والتعدينية.", "en": "Building partnerships with Arab, regional and international institutions to strengthen the position of Arab countries in the energy and mining industries."}},
        ],
        "roadmap_title": {"ar": "خارطة الطريق 2026–2030", "en": "2026–2030 Roadmap"},
        "roadmap_sub": {
            "ar": "كشفت اللجنة التأسيسية في الندوة الصحفية التي أعقبت الجمعية العمومية عن البرنامج السنوي للاتحاد وخارطة الطريق الممتدة بين 2026 و2030، والتي تهدف إلى إطلاق مبادرات ومشاريع وشراكات تخدم تنمية قطاعي الطاقة والمعادن في الدول العربية.",
            "en": "At the press conference following the General Assembly, the founding committee unveiled the Union's annual programme and its 2026–2030 roadmap, designed to launch initiatives, projects and partnerships serving the development of the energy and minerals sectors in Arab countries.",
        },
        "roadmap": [
            ("2026", {"ar": "استكمال البناء المؤسسي: تشكيل المجلس الأعلى ومجلس الإدارة والأمانة العامة واللجان المتخصصة، وإطلاق العضوية.", "en": "Completing the institutional build-out: forming the Superior Council, Board of Directors, General Secretariat and specialized commissions, and launching membership."}),
            ("2027", {"ar": "تفعيل شبكة التعاون وبناء الشراكات مع المؤسسات العربية والإقليمية والدولية وإطلاق أولى المبادرات القطاعية.", "en": "Activating the cooperation network, building partnerships with Arab, regional and international institutions, and launching first sectoral initiatives."}),
            ("2028", {"ar": "إطلاق مشاريع مهيكلة في الانتقال الطاقي والتعدين المستدام وبرامج البحث والابتكار ونقل التكنولوجيا.", "en": "Launching structured projects in energy transition and sustainable mining, and programmes for research, innovation and technology transfer."}),
            ("2029", {"ar": "تعزيز الاستثمار العربي والدولي ومواكبة تحول الفرص إلى شراكات استراتيجية ومشاريع ملموسة.", "en": "Advancing Arab and international investment and turning opportunities into strategic partnerships and concrete projects."}),
            ("2030", {"ar": "ترسيخ مكانة الاتحاد كمنصة عربية مرجعية وقياس أثر مبادراته على التنمية المستدامة والتكامل الاقتصادي.", "en": "Consolidating the Union's standing as the Arab reference platform and measuring its initiatives' impact on sustainable development and economic integration."}),
        ],
    },

    # ------------------------------------------------------------------ NEWS
    "news": {
        "title": {"ar": "الأخبار", "en": "News"},
        "meta": {
            "ar": "أخبار الاتحاد العربي للطاقة والمعادن وتغطيات تأسيسه الإعلامية.",
            "en": "News and media coverage of the Arab Union for Energy & Minerals.",
        },
        "items": [
            {"date": "2026-07-23",
             "title": {"ar": "الإعلان رسمياً عن تأسيس الاتحاد العربي للطاقة والمعادن", "en": "Arab Union for Energy & Minerals officially established"},
             "body": {"ar": "انعقدت بمدينة سلا المغربية الجمعية العمومية التأسيسية للاتحاد العربي للطاقة والمعادن، بحضور صناع قرار ومسؤولين وخبراء وفاعلين اقتصاديين يمثلون القطاع الخاص من عدة دول عربية. وانتُخب المغرب بالإجماع لرئاسة المنظمة الجديدة التي سيكون مقرها في الدار البيضاء، واختير السيد صلاح الدين البدري رئيساً للاتحاد.",
                      "en": "The inaugural General Assembly of the Arab Union for Energy & Minerals was held in Salé, Morocco, bringing together decision-makers, officials, experts and private-sector economic actors from several Arab countries. Morocco was unanimously elected to the presidency of the new organization, headquartered in Casablanca, and Salah Eddine El Badry was chosen as the Union's President."},
             "source": "MAP / Aldar"},
            {"date": "2026-07-23",
             "title": {"ar": "اللجنة التأسيسية تكشف عن البرنامج السنوي وخارطة الطريق 2026–2030", "en": "Founding committee unveils annual programme and 2026–2030 roadmap"},
             "body": {"ar": "في ندوة صحفية أعقبت الجمعية العمومية التأسيسية، أوضح المنظمون أن تأسيس الاتحاد جاء بمبادرة من شركة يونايتد بتروليوم بصفتها العضو المؤسس والشريك الاستراتيجي، وتم الكشف عن اللجنة التأسيسية والبرنامج السنوي وخارطة الطريق للفترة 2026–2030، بهدف إطلاق مبادرات ومشاريع وشراكات تخدم تنمية قطاعي الطاقة والمعادن في الدول العربية.",
                      "en": "At a press conference following the inaugural General Assembly, organizers announced that the Union was established on the initiative of United Petroleum as founding member and strategic partner. The founding committee, annual programme and 2026–2030 roadmap were unveiled, aiming to launch initiatives, projects and partnerships serving energy and minerals development across Arab countries."},
             "source": "Al Mostakbal / ConsoNews"},
            {"date": "2026-07-23",
             "title": {"ar": "إسماعيل الجنابي: تأسيس الاتحاد «لحظة تاريخية» في مسار التكامل العربي", "en": "Ismaeil Al Janaby: the Union's founding is a \"historic moment\" for Arab integration"},
             "body": {"ar": "أكد إسماعيل الجنابي، العضو المؤسس بمجلس إدارة الاتحاد، أن الإعلان الرسمي عن تأسيس الاتحاد يشكل «لحظة تاريخية» و«منعطفاً حاسماً» في مسار التكامل العربي، مشدداً على أن الركائز التأسيسية تتمحور حول دمج التكنولوجيات الجديدة وتعزيز البحث العلمي والطاقات النظيفة وخفض الانبعاثات تماشياً مع أهداف التنمية المستدامة.",
                      "en": "Ismaeil Al Janaby, founding member of the Union's Board of Directors, described the official establishment of the Union as a \"historic moment\" and a \"decisive turning point\" in Arab integration, highlighting founding pillars centered on integrating new technologies, promoting scientific research and clean energy, and reducing emissions in line with the Sustainable Development Goals."},
             "source": "Aldar"},
            {"date": "2026-07-28",
             "title": {"ar": "فدرالية الطاقة بالمغرب ترحب بميلاد الاتحاد العربي للطاقة والمعادن", "en": "Morocco's Fédération de l'Energie welcomes the Union's creation"},
             "body": {"ar": "نشرت فدرالية الطاقة بالمغرب تغطية لميلاد الاتحاد العربي للطاقة والمعادن، مسلطة الضوء على طموحه ليصبح المنصة العربية المرجعية التي تجعل من الطاقة والمعادن روافع للتنمية المستدامة والتكامل الاقتصادي الإقليمي.",
                      "en": "Morocco's Fédération de l'Energie covered the birth of the Arab Union for Energy & Minerals, highlighting its ambition to become the Arab reference platform making energy and minerals levers of sustainable development and regional economic integration."},
             "source": "Fédération de l'Energie"},
        ],
        "sources_title": {"ar": "مصادر التغطية الصحفية", "en": "Press coverage sources"},
        "sources": [
            ("وكالة المغرب العربي للأنباء / الدار", "https://aldar.ma/448235.html"),
            ("جريدة المستقبل 24", "https://almostakbal24.ma/2026/07/23/arab-energy-minerals-union-rabat/"),
            ("كونسونيوز", "https://ar.consonews.ma/31547.html"),
            ("الرباط نيوز", "https://www.ribatnews.com/artciles/102807"),
            ("MCG24 (English)", "https://en.mcg24.com/sale-establishment-of-the-arab-union-for-energy-and-mines-led-by-morocco/"),
            ("Fédération de l'Energie (Français)", "https://www.fedenerg.ma/2026/07/28/lunion-arabe-de-lenergie-et-des-mines-voit-le-jour/"),
        ],
    },

    # ----------------------------------------------------------------- UNIONS
    "unions": {
        "title": {"ar": "اتحادات عربية شقيقة", "en": "Sister Arab Unions"},
        "meta": {
            "ar": "تعرف على الاتحادات العربية النوعية المتخصصة العاملة تحت مظلة جامعة الدول العربية ومجلس الوحدة الاقتصادية العربية.",
            "en": "Discover the specialized Arab federations and unions operating under the League of Arab States and the Council of Arab Economic Unity.",
        },
        "intro_title": {"ar": "منظومة العمل العربي المشترك", "en": "The Arab joint-action ecosystem"},
        "intro": {
            "ar": "ينضم الاتحاد العربي للطاقة والمعادن إلى منظومة عريقة من الاتحادات العربية النوعية المتخصصة التي تعمل تحت مظلة جامعة الدول العربية (تأسست 1945، مقرها القاهرة وتضم 22 دولة عضواً). ويشرف مجلس الوحدة الاقتصادية العربية — الذي أنشئ بموجب اتفاقية 1957 ودخلت حيز النفاذ عام 1964 — على الاتحادات المهنية النوعية المتخصصة، كما يجمع «ملتقى الاتحادات العربية النوعية المتخصصة» (تأسس نهاية 2017 برعاية الأمين العام لجامعة الدول العربية) أكثر من 40 اتحاداً عربياً.",
            "en": "The Arab Union for Energy & Minerals joins a longstanding ecosystem of specialized Arab federations operating under the League of Arab States (founded 1945, headquartered in Cairo, with 22 member states). The Council of Arab Economic Unity — established by a 1957 agreement that entered into force in 1964 — oversees specialized professional federations, while the Forum of Specialized Arab Federations (established in late 2017 under the patronage of the League's Secretary-General) brings together more than 40 Arab unions.",
        },
        "groups": [
            {"name": {"ar": "الاتحادات الاقتصادية والصناعية", "en": "Economic & industrial unions"},
             "items": [
                 {"ar": "الاتحاد العام لغرف التجارة والصناعة والزراعة للبلاد العربية", "en": "Federation of Arab Chambers of Commerce, Industry & Agriculture", "est": "1951", "hq": {"ar": "بيروت", "en": "Beirut"}, "desc": {"ar": "يمثل الغرف التجارية والصناعية والزراعية في الدول العربية.", "en": "Represents chambers of commerce, industry and agriculture in Arab countries."}},
                 {"ar": "اتحاد المصارف العربية", "en": "Union of Arab Banks", "est": "1974", "hq": {"ar": "بيروت", "en": "Beirut"}, "desc": {"ar": "الإطار الجامع للمجتمع المصرفي والمالي العربي، تأسس بقرار من جامعة الدول العربية.", "en": "The umbrella organization of the Arab banking and financial community, established by an Arab League resolution."}},
                 {"ar": "الإتحاد العام العربي للتأمين", "en": "General Arab Insurance Federation (GAIF)", "est": "1953", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "يجمع شركات وأسواق التأمين العربية.", "en": "Brings together Arab insurance companies and markets."}},
                 {"ar": "اتحاد المقاولين العرب", "en": "Arab Contractors Federation", "est": "—", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "يمثل شركات المقاولات العربية ويعزز تكامل قطاع الإنشاءات.", "en": "Represents Arab contractors and promotes integration of the construction sector."}},
                 {"ar": "الاتحاد العربي للحديد والصلب", "en": "Arab Iron & Steel Union (AISU)", "est": "1972", "hq": {"ar": "عمّان", "en": "Amman"}, "desc": {"ar": "أول منظمة عربية متخصصة في مجال الحديد والصلب تابعة لمجلس الوحدة الاقتصادية.", "en": "The first specialized Arab organization in iron and steel under the Council of Arab Economic Unity."}},
                 {"ar": "الاتحاد العربي لمنتجي الأسمدة", "en": "Arab Fertilizer Association (AFA)", "est": "1975", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "يجمع منتجي الأسمدة العرب ويدعم تطوير الصناعة.", "en": "Brings together Arab fertilizer producers and supports the industry's development."}},
                 {"ar": "الاتحاد العربي للأسمنت ومواد البناء", "en": "Arab Union for Cement & Building Materials (AUCBM)", "est": "1977", "hq": {"ar": "دمشق", "en": "Damascus"}, "desc": {"ar": "يخدم صناعة الأسمنت ومواد البناء في الدول العربية.", "en": "Serves the cement and building-materials industry in Arab countries."}},
                 {"ar": "الاتحاد العربي لمنتجي البتروكيماويات والكيماويات", "en": "Arab Union of Petrochemical & Chemical Producers", "est": "1994", "hq": {"ar": "الكويت", "en": "Kuwait"}, "desc": {"ar": "يجمع منتجي البتروكيماويات والكيماويات العرب.", "en": "Brings together Arab petrochemical and chemical producers."}},
                 {"ar": "الاتحاد العربي للصناعات الغذائية", "en": "Arab Union for Food Industries", "est": "1995", "hq": {"ar": "—", "en": "—"}, "desc": {"ar": "يدعم تكامل صناعة الأغذية العربية وسلاسل إمدادها.", "en": "Supports the integration of the Arab food industry and its supply chains."}},
                 {"ar": "الاتحاد العربي لمنتجي وناقلي وموزعي الكهرباء", "en": "Arab Union of Electricity (AUPTDE)", "est": "1987", "hq": {"ar": "عمّان", "en": "Amman"}, "desc": {"ar": "ينسق العمل بين مؤسسات الكهرباء العربية للإنتاج والنقل والتوزيع.", "en": "Coordinates Arab electricity producers, transmitters and distributors."}},
             ]},
            {"name": {"ar": "اتحادات النقل والاتصال", "en": "Transport & communications unions"},
             "items": [
                 {"ar": "الاتحاد العربي للنقل الجوي", "en": "Arab Air Carriers' Organization (AACO)", "est": "1965", "hq": {"ar": "بيروت", "en": "Beirut"}, "desc": {"ar": "يجمع الناقلات الجوية العربية.", "en": "Brings together Arab air carriers."}},
                 {"ar": "الاتحاد العربي للسكك الحديدية", "en": "Arab Union of Railways", "est": "1979", "hq": {"ar": "حلب", "en": "Aleppo"}, "desc": {"ar": "يعزز تكامل شبكات السكك الحديدية العربية.", "en": "Promotes integration of Arab railway networks."}},
                 {"ar": "الاتحاد العربي للنقل البري", "en": "Arab Union of Land Transport", "est": "—", "hq": {"ar": "عمّان", "en": "Amman"}, "desc": {"ar": "يدعم قطاع النقل البري العربي وتسهيل حركة التجارة.", "en": "Supports the Arab land-transport sector and facilitates trade flows."}},
                 {"ar": "اتحاد إذاعات الدول العربية", "en": "Arab States Broadcasting Union (ASBU)", "est": "1969", "hq": {"ar": "تونس", "en": "Tunis"}, "desc": {"ar": "يجمع الهيئات الإذاعية والتلفزيونية العربية.", "en": "Brings together Arab radio and television corporations."}},
                 {"ar": "اتحاد وكالات الأنباء العربية", "en": "Federation of Arab News Agencies (FANA)", "est": "1975", "hq": {"ar": "—", "en": "—"}, "desc": {"ar": "ينسق التعاون بين وكالات الأنباء العربية.", "en": "Coordinates cooperation among Arab news agencies."}},
             ]},
            {"name": {"ar": "اتحادات مهنية ومجتمعية", "en": "Professional & social unions"},
             "items": [
                 {"ar": "اتحاد المحامين العرب", "en": "Arab Lawyers Union", "est": "1958", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "أقدم اتحاد مهني عربي، يجمع نقابات وهيئات المحامين.", "en": "The oldest Arab professional union, gathering bar associations and lawyers' bodies."}},
                 {"ar": "اتحاد الصحفيين العرب", "en": "Federation of Arab Journalists", "est": "1964", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "يمثل نقابات الصحفيين في الدول العربية.", "en": "Represents journalists' syndicates in Arab countries."}},
                 {"ar": "اتحاد الجامعات العربية", "en": "Association of Arab Universities", "est": "1964", "hq": {"ar": "عمّان", "en": "Amman"}, "desc": {"ar": "يجمع مئات الجامعات العربية ويدعم التعليم العالي والبحث.", "en": "Brings together hundreds of Arab universities and supports higher education and research."}},
                 {"ar": "الاتحاد العام للفلاحين والتعاونيين الزراعيين العرب", "en": "General Union of Arab Peasants & Agricultural Cooperatives", "est": "—", "hq": {"ar": "—", "en": "—"}, "desc": {"ar": "يمثل الفلاحين والجمعيات التعاونية الزراعية العربية.", "en": "Represents Arab peasants and agricultural cooperatives."}},
                 {"ar": "الاتحاد العربي للمعارض والمؤتمرات الدولية", "en": "Arab Union for International Exhibitions & Conferences (AUIEC)", "est": "1995", "hq": {"ar": "القاهرة", "en": "Cairo"}, "desc": {"ar": "يخدم صناعة المعارض والمؤتمرات العربية تحت رعاية الجامعة العربية.", "en": "Serves the Arab exhibitions and conferences industry under Arab League auspices."}},
                 {"ar": "الاتحاد العربي للطاقة والمعادن", "en": "Arab Union for Energy & Minerals (AUEM)", "est": "2026", "hq": {"ar": "الدار البيضاء", "en": "Casablanca"}, "desc": {"ar": "أحدث الاتحادات العربية النوعية — يجمع فاعلي قطاعي الطاقة والمعادن في الدول العربية.", "en": "The newest specialized Arab union — uniting energy and minerals stakeholders across Arab countries."}},
             ]},
        ],
        "orgs_title": {"ar": "منظمات عربية متخصصة تابعة للجامعة العربية", "en": "Specialized organizations of the Arab League"},
        "orgs_sub": {
            "ar": "إلى جانب الاتحادات المهنية، تضم منظومة جامعة الدول العربية منظمات متخصصة تعمل في مجالات قطاعية:",
            "en": "Alongside the professional federations, the Arab League system includes specialized sectoral organizations:",
        },
        "orgs": [
            {"ar": "المنظمة العربية للتربية والثقافة والعلوم (ألكسو)", "en": "Arab League Educational, Cultural & Scientific Organization (ALECSO)", "est": "1970", "hq": {"ar": "تونس", "en": "Tunis"}},
            {"ar": "المنظمة العربية للتنمية الزراعية", "en": "Arab Organization for Agricultural Development", "est": "1970", "hq": {"ar": "الخرطوم", "en": "Khartoum"}},
            {"ar": "المنظمة العربية للتنمية الصناعية والتقييس والتعدين", "en": "Arab Industrial Development, Standardization & Mining Organization (AIDSMO)", "est": "1968", "hq": {"ar": "الرباط", "en": "Rabat"}},
            {"ar": "المنظمة العربية للعمل", "en": "Arab Labour Organization", "est": "1965", "hq": {"ar": "القاهرة", "en": "Cairo"}},
            {"ar": "صندوق النقد العربي", "en": "Arab Monetary Fund", "est": "1976", "hq": {"ar": "أبوظبي", "en": "Abu Dhabi"}},
            {"ar": "منظمة الأقطار العربية المصدرة للبترول (أوابك)", "en": "Organization of Arab Petroleum Exporting Countries (OAPEC)", "est": "1968", "hq": {"ar": "الكويت", "en": "Kuwait"}},
            {"ar": "الوكالة العربية للطاقة الذرية", "en": "Arab Atomic Energy Agency", "est": "1989", "hq": {"ar": "تونس", "en": "Tunis"}},
            {"ar": "المنظمة العربية للطيران المدني", "en": "Arab Civil Aviation Organization", "est": "1989", "hq": {"ar": "الرباط", "en": "Rabat"}},
            {"ar": "الأكاديمية العربية للعلوم والتكنولوجيا والنقل البحري", "en": "Arab Academy for Science, Technology & Maritime Transport", "est": "1970", "hq": {"ar": "الإسكندرية", "en": "Alexandria"}},
        ],
        "note": {
            "ar": "يسعى الاتحاد العربي للطاقة والمعادن إلى بناء شراكات عمل مع هذه المنظومة، وفي مقدمتها جامعة الدول العربية والمنظمة العربية للتنمية الصناعية والتقييس والتعدين.",
            "en": "The Arab Union for Energy & Minerals seeks to build working partnerships across this ecosystem — foremost with the League of Arab States and AIDSMO.",
        },
    },

    # ---------------------------------------------------------------- CONTACT
    "contact": {
        "title": {"ar": "اتصل بنا", "en": "Contact Us"},
        "meta": {
            "ar": "تواصل مع الأمانة العامة للاتحاد العربي للطاقة والمعادن — الدار البيضاء، المغرب.",
            "en": "Contact the General Secretariat of the Arab Union for Energy & Minerals — Casablanca, Morocco.",
        },
        "intro": {
            "ar": "يسعدنا تواصلكم معنا للاستفسار عن العضوية أو الشراكات أو أي معلومات حول أنشطة الاتحاد.",
            "en": "We welcome your inquiries about membership, partnerships, or any information about the Union's activities.",
        },
        "hq_title": {"ar": "المقر الرئيسي", "en": "Headquarters"},
        "hq_value": {"ar": "الدار البيضاء، المملكة المغربية", "en": "Casablanca, Kingdom of Morocco"},
        "form_name": {"ar": "الاسم", "en": "Name"},
        "form_org": {"ar": "الجهة / الشركة", "en": "Organization / Company"},
        "form_email": {"ar": "البريد الإلكتروني", "en": "Email"},
        "form_subject": {"ar": "الموضوع", "en": "Subject"},
        "form_message": {"ar": "الرسالة", "en": "Message"},
        "form_send": {"ar": "إرسال", "en": "Send"},
        "form_note": {
            "ar": "سيتم تحويل رسالتك عبر البريد الإلكتروني إلى الأمانة العامة للاتحاد.",
            "en": "Your message will be forwarded by email to the Union's General Secretariat.",
        },
        "topics_title": {"ar": "يمكنك الاستفسار عن", "en": "You can ask about"},
        "topics": [
            {"ar": "العضوية ومتطلبات الانضمام", "en": "Membership and admission requirements"},
            {"ar": "الشراكات المؤسسية والاستثمارية", "en": "Institutional and investment partnerships"},
            {"ar": "اللجان المتخصصة وسبل المشاركة", "en": "Specialized commissions and how to participate"},
            {"ar": "الفعاليات والمؤتمرات القادمة", "en": "Upcoming events and conferences"},
            {"ar": "الاستفسارات الإعلامية والصحفية", "en": "Media and press inquiries"},
        ],
    },
}

FOOTER = {
    "about": {
        "ar": "منصة مؤسسية عربية تهدف إلى دفع العمل العربي المشترك في قطاعي الطاقة والمعادن، تأسست في يوليو 2026 ويتخذ من الدار البيضاء مقراً له.",
        "en": "A pan-Arab institutional platform advancing joint Arab action in the energy and minerals sectors. Founded July 2026, headquartered in Casablanca.",
    },
    "links_title": {"ar": "روابط سريعة", "en": "Quick links"},
    "contact_title": {"ar": "تواصل", "en": "Contact"},
    "rights": {"ar": "جميع الحقوق محفوظة", "en": "All rights reserved"},
    "disclaimer": {
        "ar": "محتوى تعريفي مستند إلى التغطيات الصحفية الرسمية لإعلان التأسيس.",
        "en": "Informational content based on official press coverage of the founding announcement.",
    },
}

CHATBOT = {
    "name": {"ar": "مساعد الاتحاد", "en": "AUEM Assistant"},
    "greeting": {
        "ar": "مرحباً! أنا المساعد الذكي للاتحاد العربي للطاقة والمعادن. اسألني عن تأسيس الاتحاد، أهدافه، هيكله، العضوية، أنشطته، أو الاتحادات العربية الشقيقة.",
        "en": "Hello! I'm the AI assistant of the Arab Union for Energy & Minerals. Ask me about the Union's founding, objectives, structure, membership, activities, or sister Arab unions.",
    },
    "placeholder": {"ar": "اكتب سؤالك هنا…", "en": "Type your question here…"},
    "suggestions": [
        {"ar": "متى تأسس الاتحاد؟", "en": "When was the Union founded?"},
        {"ar": "ما هي أهداف الاتحاد؟", "en": "What are the Union's objectives?"},
        {"ar": "كيف أنضم للاتحاد؟", "en": "How can I join the Union?"},
        {"ar": "أين مقر الاتحاد؟", "en": "Where is the Union headquartered?"},
    ],
    "fallback": {
        "ar": "عذراً، لا تتوفر لديّ إجابة دقيقة عن هذا السؤال حالياً. جرّب صياغة أخرى أو اسأل عن: التأسيس، الأهداف، الهيكل التنظيمي، العضوية، الأنشطة، الأخبار، أو الاتحادات العربية الأخرى.",
        "en": "Sorry, I don't have a precise answer for that yet. Try rephrasing, or ask about: founding, objectives, governance, membership, activities, news, or other Arab unions.",
    },
}

# Chatbot knowledge base — each entry: keywords (ar & en) + answer (ar & en).
KB = [
    {"kw_ar": ["تأسس", "تأسيس", "متى", "نشأة", "انطلق", "تاريخ"], "kw_en": ["found", "establish", "when", "created", "launch", "inception", "history"],
     "a_ar": "أُعلن رسمياً عن تأسيس الاتحاد العربي للطاقة والمعادن في 23 يوليو 2026 خلال الجمعية العمومية التأسيسية التي انعقدت في مدينة سلا بالمملكة المغربية، بحضور فاعلين اقتصاديين وخبراء من عدة دول عربية.",
     "a_en": "The Arab Union for Energy & Minerals was officially founded on 23 July 2026 at its inaugural General Assembly held in Salé, Kingdom of Morocco, attended by economic actors and experts from several Arab countries."},
    {"kw_ar": ["مقر", "مكان", "أين", "الدار البيضاء", "عنوان"], "kw_en": ["headquarter", "where", "located", "address", "casablanca", "hq"],
     "a_ar": "يقع المقر الرئيسي للاتحاد في مدينة الدار البيضاء بالمملكة المغربية، وقد انتُخب المغرب بالإجماع لرئاسة الاتحاد.",
     "a_en": "The Union's headquarters is in Casablanca, Kingdom of Morocco. Morocco was unanimously elected to the Union's presidency."},
    {"kw_ar": ["رئيس", "الرئاسة", "البدري", "من يرأس"], "kw_en": ["president", "chair", "who leads", "badry", "leadership"],
     "a_ar": "رئيس الاتحاد هو السيد صلاح الدين البدري، وقد انتُخبت المملكة المغربية بالإجماع لرئاسة الاتحاد خلال الجمعية العمومية التأسيسية. ومن أبرز الأعضاء المؤسسين إسماعيل الجنابي بمجلس الإدارة، وشركة يونايتد بتروليوم كعضو مؤسس وشريك استراتيجي.",
     "a_en": "The Union's President is Salah Eddine El Badry; Morocco was unanimously elected to the presidency at the inaugural General Assembly. Notable founders include Ismaeil Al Janaby (founding Board member) and United Petroleum (founding member and strategic partner)."},
    {"kw_ar": ["هدف", "أهداف", "غايات", "يسعى"], "kw_en": ["objective", "goal", "aim", "mission", "purpose"],
     "a_ar": "تشمل أهداف الاتحاد: تعزيز التكامل العربي في قطاعي الطاقة والمعادن، تشجيع الاستثمارات العربية والدولية، تعزيز الأمن الطاقي والتدبير المستدام للموارد، مواكبة الانتقال الطاقي (الطاقات المتجددة، الهيدروجين الأخضر، كفاءة الطاقة)، تطوير قطاع التعدين وفق أفضل الممارسات الدولية، وتحفيز البحث والابتكار ونقل التكنولوجيا والدبلوماسية الاقتصادية العربية.",
     "a_en": "The Union's objectives include: strengthening Arab integration in energy and minerals; promoting Arab and international investment; reinforcing Arab energy security and sustainable resource management; supporting the energy transition (renewables, green hydrogen, efficiency); developing mining to international best practices; and stimulating research, innovation, technology transfer and Arab economic diplomacy."},
    {"kw_ar": ["هيكل", "حكامة", "مجلس", "أمانة", "لجان", "تنظيم"], "kw_en": ["structure", "governance", "council", "secretariat", "commission", "board", "organ"],
     "a_ar": "يعتمد الاتحاد حكامة متكاملة تضم: المجلس الأعلى، مجلس الإدارة، الأمانة العامة، والمجلس الاستشاري الدولي، إضافة إلى ثماني لجان متخصصة تغطي: الطاقة، النفط، الغاز، المعادن، الطاقات المتجددة، الاستثمار، الابتكار وريادة الأعمال، والعلاقات الدولية.",
     "a_en": "The Union has an integrated governance structure: a Superior Council, Board of Directors, General Secretariat and International Advisory Council, plus eight specialized commissions covering energy, oil, gas, minerals, renewable energies, investment, innovation & entrepreneurship, and international relations."},
    {"kw_ar": ["عضوية", "انضمام", "انضم", "اشتراك"], "kw_en": ["member", "join", "membership", "subscription", "admission"],
     "a_ar": "عضوية الاتحاد مفتوحة للفاعلين الاقتصاديين من القطاع الخاص في الدول العربية بقطاعي الطاقة والمعادن: الشركات والمؤسسات والمستثمرين ومراكز البحث والجامعات والخبراء. للانضمام، تواصل مع الأمانة العامة عبر صفحة «اتصل بنا». إطار العضوية قيد الاعتماد ضمن خارطة الطريق 2026–2030.",
     "a_en": "Membership is open to private-sector economic actors in Arab countries working in energy and minerals: companies, institutions, investors, research centers, universities and experts. To join, contact the General Secretariat via the Contact page. The membership framework is being finalized under the 2026–2030 roadmap."},
    {"kw_ar": ["نشاط", "أنشطة", "فعاليات", "مشاريع", "مبادرات", "برامج"], "kw_en": ["activit", "program", "initiative", "project", "work", "event"],
     "a_ar": "تشمل مجالات عمل الاتحاد: بناء شبكة تعاون عربية في الطاقة والمعادن، تشجيع الاستثمار، دعم الانتقال الطاقي (الطاقات المتجددة والهيدروجين الأخضر وكفاءة الطاقة)، تطوير التعدين المستدام، تحفيز البحث والابتكار ونقل التكنولوجيا، وتعزيز الدبلوماسية الاقتصادية العربية. يمكنك الاطلاع على التفاصيل في صفحة الأنشطة.",
     "a_en": "The Union's workstreams include: building an Arab cooperation network in energy and minerals; promoting investment; supporting the energy transition (renewables, green hydrogen, efficiency); developing sustainable mining; stimulating research, innovation and technology transfer; and advancing Arab economic diplomacy. See the Activities page for details."},
    {"kw_ar": ["خارطة", "طريق", "2030", "2026", "برنامج"], "kw_en": ["roadmap", "2030", "2026", "program", "plan"],
     "a_ar": "كشفت اللجنة التأسيسية عن البرنامج السنوي للاتحاد وخارطة الطريق 2026–2030 التي تهدف إلى إطلاق مبادرات ومشاريع وشراكات تخدم تنمية قطاعي الطاقة والمعادن في الدول العربية، بدءاً باستكمال البناء المؤسسي وإطلاق العضوية.",
     "a_en": "The founding committee unveiled the Union's annual programme and 2026–2030 roadmap, which aims to launch initiatives, projects and partnerships serving energy and minerals development in Arab countries — starting with completing the institutional build-out and launching membership."},
    {"kw_ar": ["جامعة", "الدول العربية", "شراكة", "شراكات", "منظمة"], "kw_en": ["league", "arab states", "partner", "organization", "aidsmo", "las"],
     "a_ar": "يعمل الاتحاد على بناء شراكات مع مؤسسات عربية وإقليمية ودولية، من بينها جامعة الدول العربية، والمنظمة العربية للتنمية الصناعية والتقييس والتعدين، والبنك الإسلامي للتنمية، والبنك الإفريقي للتنمية، والاتحاد الإفريقي، إضافة إلى شركات الطاقة والتعدين ومراكز البحث والجامعات.",
     "a_en": "The Union is building partnerships with Arab, regional and international institutions — including the League of Arab States, AIDSMO, the Islamic Development Bank, the African Development Bank and the African Union — as well as energy and mining companies, research centers and universities."},
    {"kw_ar": ["اتحادات", "شقيقة", "أخرى", "نظيرة"], "kw_en": ["union", "federation", "sister", "other", "similar"],
     "a_ar": "تحت مظلة جامعة الدول العربية ومجلس الوحدة الاقتصادية العربية تعمل أكثر من 40 اتحاداً عربياً نوعياً متخصصاً، منها: اتحاد المصارف العربية (1974)، الاتحاد العام لغرف التجارة والصناعة والزراعة (1951)، الاتحاد العربي للحديد والصلب (1972)، الاتحاد العربي للكهرباء (1987)، والاتحاد العربي للأسمدة (1975). تصفح صفحة «اتحادات عربية» للقائمة الكاملة.",
     "a_en": "More than 40 specialized Arab unions operate under the League of Arab States and the Council of Arab Economic Unity, including the Union of Arab Banks (1974), the Federation of Arab Chambers (1951), the Arab Iron & Steel Union (1972), the Arab Union of Electricity (1987) and the Arab Fertilizer Association (1975). Browse the 'Arab Unions' page for the full list."},
    {"kw_ar": ["قطاع", "مجالات", "طاقة", "معادن", "تعدين", "نفط", "غاز"], "kw_en": ["sector", "field", "energy", "mineral", "mining", "oil", "gas", "industry"],
     "a_ar": "يعمل الاتحاد في قطاعين استراتيجيين مترابطين: الطاقة (بما فيها النفط والغاز والطاقات المتجددة والهيدروجين الأخضر) والمعادن والتعدين، بهدف تحويل موارد العالم العربي الطاقية والمعدنية إلى مشاريع وشراكات وفرص استثمارية.",
     "a_en": "The Union works across two linked strategic sectors: energy (including oil, gas, renewables and green hydrogen) and minerals & mining — aiming to turn the Arab world's energy and mineral resources into projects, partnerships and investment opportunities."},
    {"kw_ar": ["متجددة", "هيدروجين", "انبعاثات", "نظيفة", "استدامة"], "kw_en": ["renewable", "hydrogen", "emission", "clean", "sustainab", "green", "transition"],
     "a_ar": "يواكب الاتحاد الانتقال الطاقي عبر دعم مشاريع الطاقة المتجددة والهيدروجين الأخضر وكفاءة الطاقة، وخفض الانبعاثات تماشياً مع أهداف التنمية المستدامة — وهي من الركائز التأسيسية للاتحاد.",
     "a_en": "The Union supports the energy transition through renewable-energy, green-hydrogen and energy-efficiency projects, and emissions reduction in line with the Sustainable Development Goals — all among its founding pillars."},
    {"kw_ar": ["اتصل", "تواصل", "بريد", "هاتف", "ايميل"], "kw_en": ["contact", "email", "phone", "reach", "call"],
     "a_ar": "يمكنك التواصل مع الأمانة العامة للاتحاد عبر نموذج الاتصال في صفحة «اتصل بنا». المقر الرئيسي: الدار البيضاء، المملكة المغربية.",
     "a_en": "You can reach the Union's General Secretariat through the contact form on the Contact page. Headquarters: Casablanca, Kingdom of Morocco."},
    {"kw_ar": ["اخبار", "أخبار", "جديد", "مستجدات"], "kw_en": ["news", "latest", "update", "press"],
     "a_ar": "أحدث أخبار الاتحاد تتعلق بإعلان تأسيسه في يوليو 2026 والكشف عن اللجنة التأسيسية والبرنامج السنوي وخارطة الطريق 2026–2030. تفاصيل أكثر في صفحة الأخبار مع روابط التغطيات الصحفية.",
     "a_en": "The Union's latest news covers its founding announcement in July 2026 and the unveiling of its founding committee, annual programme and 2026–2030 roadmap. See the News page for details and press coverage links."},
    {"kw_ar": ["يونايتد", "بتروليوم", "مؤسس", "شريك"], "kw_en": ["united petroleum", "founding", "strategic partner"],
     "a_ar": "تأسس الاتحاد بمبادرة من شركة يونايتد بتروليوم بصفتها العضو المؤسس والشريك الاستراتيجي، وكشفت الجمعية العمومية التأسيسية عن اللجنة التأسيسية التي تقود البناء المؤسسي للاتحاد.",
     "a_en": "The Union was established on the initiative of United Petroleum as founding member and strategic partner. The inaugural General Assembly unveiled the founding committee leading the Union's institutional build-out."},
    {"kw_ar": ["من", "ما هو", "ماذا", "تعريف"], "kw_en": ["what is", "who is", "about", "definition", "auem"],
     "a_ar": "الاتحاد العربي للطاقة والمعادن (AUEM) منظمة مهنية عربية تأسست في 23 يوليو 2026 بمدينة سلا المغربية، ومقرها الدار البيضاء. تهدف إلى أن تصبح المنصة العربية المرجعية التي تجعل من الطاقة والمعادن روافع للتنمية المستدامة والتكامل الاقتصادي الإقليمي.",
     "a_en": "The Arab Union for Energy & Minerals (AUEM) is a pan-Arab professional organization founded on 23 July 2026 in Salé, Morocco, headquartered in Casablanca. It aims to become the Arab reference platform making energy and minerals levers of sustainable development and regional economic integration."},
]
