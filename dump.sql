--
-- PostgreSQL database dump
--

-- Dumped from database version 13.12
-- Dumped by pg_dump version 13.12

-- Started on 2024-05-22 10:10:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 25366)
-- Name: AttributeValue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."AttributeValue" (
    id integer NOT NULL,
    product_id integer NOT NULL,
    attribute_id integer NOT NULL,
    value character varying NOT NULL
);


ALTER TABLE public."AttributeValue" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 25364)
-- Name: AttributeValue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."AttributeValue_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."AttributeValue_id_seq" OWNER TO postgres;

--
-- TOC entry 3060 (class 0 OID 0)
-- Dependencies: 209
-- Name: AttributeValue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."AttributeValue_id_seq" OWNED BY public."AttributeValue".id;


--
-- TOC entry 200 (class 1259 OID 16530)
-- Name: Category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Category" (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public."Category" OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16536)
-- Name: Category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Category_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Category_id_seq" OWNER TO postgres;

--
-- TOC entry 3061 (class 0 OID 0)
-- Dependencies: 201
-- Name: Category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Category_id_seq" OWNED BY public."Category".id;


--
-- TOC entry 202 (class 1259 OID 16538)
-- Name: Orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Orders" (
    id integer NOT NULL,
    user_id integer NOT NULL,
    product_id integer NOT NULL
);


ALTER TABLE public."Orders" OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16541)
-- Name: Orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Orders_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Orders_id_seq" OWNER TO postgres;

--
-- TOC entry 3062 (class 0 OID 0)
-- Dependencies: 203
-- Name: Orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Orders_id_seq" OWNED BY public."Orders".id;


--
-- TOC entry 206 (class 1259 OID 25339)
-- Name: ProductAttributes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."ProductAttributes" (
    id integer NOT NULL,
    title character varying NOT NULL
);


ALTER TABLE public."ProductAttributes" OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 25337)
-- Name: ProductAttributes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."ProductAttributes_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductAttributes_id_seq" OWNER TO postgres;

--
-- TOC entry 3063 (class 0 OID 0)
-- Dependencies: 205
-- Name: ProductAttributes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."ProductAttributes_id_seq" OWNED BY public."ProductAttributes".id;


--
-- TOC entry 208 (class 1259 OID 25350)
-- Name: Products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Products" (
    id integer NOT NULL,
    title character varying NOT NULL,
    category integer NOT NULL,
    product_code integer NOT NULL,
    image character varying NOT NULL,
    price integer NOT NULL,
    sale boolean NOT NULL
);


ALTER TABLE public."Products" OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 25348)
-- Name: Products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Products_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Products_id_seq" OWNER TO postgres;

--
-- TOC entry 3064 (class 0 OID 0)
-- Dependencies: 207
-- Name: Products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Products_id_seq" OWNED BY public."Products".id;


--
-- TOC entry 204 (class 1259 OID 16559)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 25426)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying,
    username character varying,
    registered_at date,
    hashed_password character varying,
    is_active boolean,
    is_superuser boolean,
    is_verified boolean,
    image character varying
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 25424)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."user" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2893 (class 2604 OID 25369)
-- Name: AttributeValue id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."AttributeValue" ALTER COLUMN id SET DEFAULT nextval('public."AttributeValue_id_seq"'::regclass);


--
-- TOC entry 2889 (class 2604 OID 16572)
-- Name: Category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Category" ALTER COLUMN id SET DEFAULT nextval('public."Category_id_seq"'::regclass);


--
-- TOC entry 2890 (class 2604 OID 16573)
-- Name: Orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders" ALTER COLUMN id SET DEFAULT nextval('public."Orders_id_seq"'::regclass);


--
-- TOC entry 2891 (class 2604 OID 25342)
-- Name: ProductAttributes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ProductAttributes" ALTER COLUMN id SET DEFAULT nextval('public."ProductAttributes_id_seq"'::regclass);


--
-- TOC entry 2892 (class 2604 OID 25353)
-- Name: Products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Products" ALTER COLUMN id SET DEFAULT nextval('public."Products_id_seq"'::regclass);


--
-- TOC entry 3052 (class 0 OID 25366)
-- Dependencies: 210
-- Data for Name: AttributeValue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."AttributeValue" (id, product_id, attribute_id, value) FROM stdin;
1	1	1	Китай\n
2	1	2	2
3	1	3	4
4	1	4	Кордура
5	1	5	12
6	1	6	Красный
7	1	7	Grizzly
8	2	7	Lakestone
9	2	6	Черный
10	2	5	12
11	2	4	Флис
12	2	3	4
13	2	2	2
14	2	1	Китай
15	5	7	Lakestone
16	5	6	Желтый
17	5	5	12
18	5	4	Кордура
19	5	3	4
20	5	2	2
21	5	1	США
22	6	7	Bobby XD Design
23	6	6	Песочный
24	6	5	12
25	6	4	Флис
26	6	3	4
27	6	2	2
28	6	1	Россия
29	7	7	Grizzly
30	7	6	Серый
31	7	5	12
32	7	4	Арамид
33	7	3	4
34	7	2	2
35	7	1	Россия
36	8	7	Lakestone
37	8	6	Черный
38	8	5	12
39	8	4	Неопрен
40	8	3	4
41	8	2	2
42	8	1	Россия
43	9	7	Grizzly
44	9	6	Черный
45	9	5	12
46	9	4	Неопрен
47	9	3	4
48	9	2	2
49	9	1	США
50	10	7	Bobby XD Design
51	10	6	Черный
52	10	5	12
53	10	4	Неопрен
54	10	3	4
55	10	2	2
56	10	1	Китай
57	11	7	Lakestone
58	11	6	Черный
59	11	5	12
60	11	4	Неопрен
61	11	3	4
62	11	2	2
63	11	1	Россия
64	12	7	Lakestone
65	12	6	Черный
66	12	5	12
67	12	4	Неопрен
68	12	3	4
69	12	2	2
70	12	1	Россия
71	13	1	Китай
72	13	2	2
73	13	3	4
74	13	8	1
75	13	9	40
76	13	10	Двухтактный
77	13	11	2007
78	14	1	Китай
79	14	2	2
80	14	3	4
81	14	8	1
82	14	9	40
83	14	10	Двухтактный
84	14	11	2007
85	27	1	США
86	27	2	2
87	27	3	4
88	27	8	1
89	27	9	35
90	27	10	Двухтактный
91	27	11	2005
92	26	1	Россия
93	26	2	2
94	26	3	4
95	26	8	1
96	26	9	50
97	26	10	Двухтактный
98	26	11	2012
99	25	1	Китай
100	25	2	2
101	25	3	4
102	25	8	1
103	25	9	45
104	25	10	Двухтактный
105	25	11	2010
106	24	1	Китай
107	24	2	2
108	24	3	4
109	24	8	1
110	24	9	40
111	24	10	Двухтактный
112	24	11	2007
113	23	1	США
114	23	2	2
115	23	3	4
116	23	8	1
117	23	9	55
118	23	10	Двухтактный
119	23	11	2000
120	22	1	Россия
121	22	2	2
122	22	3	4
123	22	8	1
124	22	9	40
125	22	10	Двухтактный
126	22	11	2007
127	21	1	США
128	21	2	2
129	21	3	4
130	21	8	1
131	21	9	30
132	21	10	Двухтактный
133	21	11	2003
134	20	1	Китай
135	20	2	2
136	20	3	4
137	20	8	1
138	20	9	40
139	20	10	Четырехтактный
140	20	11	2007
141	19	1	США
142	19	2	2
143	19	3	4
144	19	8	1
145	19	9	40
146	19	10	Четырехтактный
147	19	11	2010
148	18	1	Китай
149	18	2	2
150	18	3	4
151	18	8	1
152	18	9	40
153	18	10	Двухтактный
154	18	11	2008
155	17	1	Россия
156	17	2	2
157	17	3	4
158	17	8	1
159	17	9	35
160	17	10	Четырехтактный
161	17	11	2009
162	16	1	Китай
163	16	2	2
164	16	3	4
165	16	8	2
166	16	9	240
167	16	10	Двухтактный
168	16	11	2007
169	15	1	Россия
170	15	2	2
171	15	3	4
172	15	8	1
173	15	9	250
174	15	10	Четырехтактный
175	15	11	2015
\.


--
-- TOC entry 3042 (class 0 OID 16530)
-- Dependencies: 200
-- Data for Name: Category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Category" (id, name) FROM stdin;
8	engines
1	Рюкзаки
2	Гидрокостюмы
3	Квадроциклы
4	Гидроциклы
5	Катера
6	Снегоходы
7	Вездеходы
9	Яхты
\.


--
-- TOC entry 3044 (class 0 OID 16538)
-- Dependencies: 202
-- Data for Name: Orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Orders" (id, user_id, product_id) FROM stdin;
\.


--
-- TOC entry 3048 (class 0 OID 25339)
-- Dependencies: 206
-- Data for Name: ProductAttributes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."ProductAttributes" (id, title) FROM stdin;
1	Страна производитель
2	В наличии
3	Рейтинг
4	Материал
5	Гарантия
6	Цвет
7	Компания
8	Кол-во мест
9	Лошадиные силы
10	Тип двигателя
11	Год выпуска
\.


--
-- TOC entry 3050 (class 0 OID 25350)
-- Dependencies: 208
-- Data for Name: Products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Products" (id, title, category, product_code, image, price, sale) FROM stdin;
1	Рюкзак 1	1	111111	bag1.jpg	7500	t
2	Рюкзак 2	1	111111	bag2.jpg	11000	f
5	Рюкзак 3	1	111111	bag3.jpg	12500	f
6	Рюкзак 4	1	111111	bag4.jpg	9500	f
7	Рюкзак 5	1	111111	bag5.jpg	8500	f
8	Гидрокостюм 1	2	111111	gidro1.jpg	8000	f
9	Гидрокостюм 5	2	111111	gidro5.jpg	15000	f
10	Гидрокостюм 4	2	111111	gidro4.jpg	13000	f
11	Гидрокостюм 3	2	111111	gidro3.jpg	12000	f
12	Гидрокостюм 2	2	111111	gidro2.jpg	9000	f
14	Квадроцикл 2	3	111111	quad2.jpg	500000	f
20	Квадроцикл 10	3	111111	quad10.jpg	500000	f
21	Квадроцикл 9	3	111111	quad9.jpg	420000	f
26	Квадроцикл 4	3	111111	quad4.jpg	650000	f
27	Квадроцикл 3	3	111111	quad3.jpg	550000	f
13	Квадроцикл 1	3	111111	quad1.png	475000	f
18	Квадроцикл 12	3	111111	quad12.png	500000	f
22	Квадроцикл 8	3	111111	quad8.png	560000	f
23	Квадроцикл 7	3	111111	quad7.png	720000	f
24	Квадроцикл 6	3	111111	quad6.png	480000	t
25	Квадроцикл 5	3	111111	quad5.png	450000	f
19	Квадроцикл 11	3	111111	quad11.webp	490000	f
17	Квадроцикл 13	3	111111	quad13.png	450000	f
15	Гидроцикл 2	4	111111	jet2.png	2450000	f
16	Гидроцикл 1	4	111111	jet1.png	2450000	f
\.


--
-- TOC entry 3046 (class 0 OID 16559)
-- Dependencies: 204
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
ee29593b6e40
\.


--
-- TOC entry 3054 (class 0 OID 25426)
-- Dependencies: 212
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, email, username, registered_at, hashed_password, is_active, is_superuser, is_verified, image) FROM stdin;
5	string	string	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$LRNe4A/QEV1KNa0OcbQ6Ew$6n2XUn3ZNZFuk6/CpotcBHfVCgXnJt3/hgfcGa8JnXM	t	f	f	default_pfp.png
6	strisddsng	stridsdsng	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$VU1ZgjL/Ml6GfpjuR8H4QQ$Spt/eNpPL6ARo/sefUq5Fawh1nArSuhUCkadykbYN9o	t	f	f	default_pfp.png
7	sds@mail.ru	dsdsds	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$HhKG76WD3Lmy65IgyIGwSw$Ku9+eYaloejMDdRg00vRf4JZwoFiBHVUqEib7TnXq2Q	t	f	f	default_pfp.png
8	string@mail.ru	string	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$+KLH4kyw0bieBJush/jdIQ$bFE9zlbxzbhlLMHTWyszdeORSNk7Vg+l5WmjGDvvA7k	t	f	f	default_pfp.png
9	string1@mail.ru	string1	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$ogIUcTFN3WdIpbIz/GGtBg$lPqy09w+PLsL8DhrLrT/mL5+aPnJE7oh1deE0MhlIVA	t	f	f	default_pfp.png
10	string2@mail.ru	string2	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$cC2cnp8tO2mKqaIWzsDZTQ$dMqvNbWa1oKwTyWILLJU3aldyouyL7wx/KbE3+DIlpM	t	f	f	default_pfp.png
11	string123@mail.ru	string123	2024-05-19	$argon2id$v=19$m=65536,t=3,p=4$d/almntteFVF+rhh5T5m1w$nVgo/a2llGWn7W/T2zrv7JMW8/yfPJ7KOkCNYZRfZTk	t	f	f	default_pfp.png
\.


--
-- TOC entry 3065 (class 0 OID 0)
-- Dependencies: 209
-- Name: AttributeValue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."AttributeValue_id_seq"', 175, true);


--
-- TOC entry 3066 (class 0 OID 0)
-- Dependencies: 201
-- Name: Category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Category_id_seq"', 9, true);


--
-- TOC entry 3067 (class 0 OID 0)
-- Dependencies: 203
-- Name: Orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Orders_id_seq"', 1, false);


--
-- TOC entry 3068 (class 0 OID 0)
-- Dependencies: 205
-- Name: ProductAttributes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."ProductAttributes_id_seq"', 11, true);


--
-- TOC entry 3069 (class 0 OID 0)
-- Dependencies: 207
-- Name: Products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Products_id_seq"', 27, true);


--
-- TOC entry 3070 (class 0 OID 0)
-- Dependencies: 211
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 11, true);


--
-- TOC entry 2905 (class 2606 OID 25371)
-- Name: AttributeValue AttributeValue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."AttributeValue"
    ADD CONSTRAINT "AttributeValue_pkey" PRIMARY KEY (id);


--
-- TOC entry 2895 (class 2606 OID 16582)
-- Name: Category Category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Category"
    ADD CONSTRAINT "Category_pkey" PRIMARY KEY (id);


--
-- TOC entry 2897 (class 2606 OID 16584)
-- Name: Orders Orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_pkey" PRIMARY KEY (id);


--
-- TOC entry 2901 (class 2606 OID 25347)
-- Name: ProductAttributes ProductAttributes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ProductAttributes"
    ADD CONSTRAINT "ProductAttributes_pkey" PRIMARY KEY (id);


--
-- TOC entry 2903 (class 2606 OID 25358)
-- Name: Products Products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Products"
    ADD CONSTRAINT "Products_pkey" PRIMARY KEY (id);


--
-- TOC entry 2899 (class 2606 OID 16590)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 2907 (class 2606 OID 25435)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 2910 (class 2606 OID 25372)
-- Name: AttributeValue AttributeValue_attribute_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."AttributeValue"
    ADD CONSTRAINT "AttributeValue_attribute_id_fkey" FOREIGN KEY (attribute_id) REFERENCES public."ProductAttributes"(id) ON DELETE CASCADE;


--
-- TOC entry 2911 (class 2606 OID 25377)
-- Name: AttributeValue AttributeValue_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."AttributeValue"
    ADD CONSTRAINT "AttributeValue_product_id_fkey" FOREIGN KEY (product_id) REFERENCES public."Products"(id) ON DELETE CASCADE;


--
-- TOC entry 2908 (class 2606 OID 25382)
-- Name: Orders Orders_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_product_id_fkey" FOREIGN KEY (product_id) REFERENCES public."Products"(id) ON DELETE CASCADE;


--
-- TOC entry 2909 (class 2606 OID 25359)
-- Name: Products Products_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Products"
    ADD CONSTRAINT "Products_category_fkey" FOREIGN KEY (category) REFERENCES public."Category"(id) ON DELETE CASCADE;


-- Completed on 2024-05-22 10:10:01

--
-- PostgreSQL database dump complete
--

