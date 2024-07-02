--
-- PostgreSQL database dump
--

-- Dumped from database version 13.12
-- Dumped by pg_dump version 13.12

-- Started on 2024-07-02 22:35:49

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
176	28	1	Россия
177	28	2	2
178	28	3	4
179	28	8	1
180	28	9	40
181	28	10	Четырехтактный
182	28	11	2015
183	37	1	Россия
184	37	2	2
185	37	3	4
186	37	8	1
187	37	9	40
188	37	10	Четырехтактный
189	37	11	2015
190	36	1	Китай
191	36	2	2
192	36	3	4
193	36	8	1
194	36	9	40
195	36	10	Четырехтактный
196	36	11	2015
197	35	1	Россия
198	35	2	2
199	35	3	4
200	35	8	1
201	35	9	40
202	35	10	Четырехтактный
203	35	11	2015
204	34	1	Россия
205	34	2	2
206	34	3	4
207	34	8	1
208	34	9	40
209	34	10	Четырехтактный
210	34	11	2015
211	33	1	США
212	33	2	2
213	33	3	4
214	33	8	1
215	33	9	40
216	33	10	Четырехтактный
217	33	11	2015
218	32	1	США
219	32	2	2
220	32	3	4
221	32	8	1
222	32	9	40
223	32	10	Четырехтактный
224	32	11	2015
225	31	1	Россия
226	31	2	2
227	31	3	4
228	31	8	1
229	31	9	40
230	31	10	Четырехтактный
231	31	11	2015
232	30	1	Россия
233	30	2	2
234	30	3	4
235	30	8	1
236	30	9	40
237	30	10	Четырехтактный
238	30	11	2015
239	29	1	Россия
240	29	2	2
241	29	3	4
242	29	8	1
243	29	9	40
244	29	10	Четырехтактный
245	29	11	2015
246	38	1	Россия
247	38	2	2
248	38	3	4
249	38	8	1
250	38	9	40
251	38	10	Четырехтактный
252	38	11	2015
253	39	1	Россия
254	39	2	2
255	39	3	4
256	39	8	1
257	39	9	40
258	39	10	Четырехтактный
259	39	11	2015
260	40	1	Россия
261	40	2	2
262	40	3	4
263	40	8	1
264	40	9	40
265	40	10	Четырехтактный
266	40	11	2015
267	41	1	Россия
268	41	2	2
269	41	3	4
270	41	8	1
271	41	9	40
272	41	10	Четырехтактный
273	41	11	2015
274	42	1	Россия
275	42	2	2
276	42	3	4
277	42	8	1
278	42	9	40
279	42	10	Четырехтактный
280	42	11	2015
281	43	1	Россия
282	43	2	2
283	43	3	4
284	43	8	1
285	43	9	40
286	43	10	Четырехтактный
287	43	11	2015
288	44	1	Россия
289	44	2	2
290	44	3	4
291	44	8	1
292	44	9	40
293	44	10	Четырехтактный
294	44	11	2015
295	45	1	Россия
296	45	2	2
297	45	3	4
298	45	8	1
299	45	9	40
300	45	10	Четырехтактный
301	45	11	2015
302	46	1	Россия
303	46	2	2
304	46	3	4
305	46	8	1
306	46	9	40
307	46	10	Четырехтактный
308	46	11	2015
309	47	1	Россия
310	47	2	2
311	47	3	4
312	47	8	1
313	47	9	40
314	47	10	Четырехтактный
315	47	11	2015
316	48	1	Россия
317	48	2	2
318	48	3	4
319	48	8	1
320	48	9	40
321	48	10	Четырехтактный
322	48	11	2015
323	49	1	Россия
324	49	2	2
325	49	3	4
326	49	8	1
327	49	9	40
328	49	10	Четырехтактный
329	49	11	2015
330	50	1	Россия
331	50	2	2
332	50	3	4
333	50	8	1
334	50	9	40
335	50	10	Четырехтактный
336	50	11	2015
337	51	1	Россия
338	51	2	2
339	51	3	4
340	51	8	1
341	51	9	40
342	51	10	Четырехтактный
343	51	11	2015
344	52	1	Россия
345	52	2	2
346	52	3	4
347	52	8	1
348	52	9	40
349	52	10	Четырехтактный
350	52	11	2015
351	53	1	Россия
352	53	2	2
353	53	3	4
354	53	8	1
355	53	9	40
356	53	10	Четырехтактный
357	53	11	2015
358	54	1	Россия
359	54	2	2
360	54	3	4
361	54	8	1
362	54	9	40
363	54	10	Четырехтактный
364	54	11	2015
365	55	1	Россия
366	55	2	2
367	55	3	4
368	55	8	1
369	55	9	40
370	55	10	Четырехтактный
371	55	11	2015
372	56	1	Россия
373	56	2	2
374	56	3	4
375	56	8	1
376	56	9	300
377	56	10	Четырехтактный
378	56	11	2015
379	57	1	Россия
380	57	2	2
381	57	3	4
382	57	8	1
383	57	9	340
384	57	10	Четырехтактный
385	57	11	2015
386	58	1	Россия
387	58	2	2
388	58	3	4
389	58	8	1
390	58	9	330
391	58	10	Четырехтактный
392	58	11	2015
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
38	Катер 3	5	111111	boat3.jpg	560000	f
39	Катер 4	5	111111	boat4.jpg	1560000	f
40	Катер 5\n	5	111111	boat5.jpg	1320000	f
41	Катер 6	5	111111	boat6.jpg	1530000	f
42	Катер 7	5	111111	boat7.jpg	1000000	f
43	Катер 8	5	111111	boat8.jpg	1650000	f
44	Катер 9	5	111111	boat9.png	1560000	f
45	Катер 10	5	111111	boat10.png	1000000	f
46	Катер 11	5	111111	boat11.jpg	1110000	f
47	Катер 12	5	111111	boat12.jpg	1760000	f
48	Катер 2	5	111111	boat2.png	1250000	f
49	Катер 1	5	111111	boat1.png	1760000	f
50	Снегоход 1	6	111111	snow1.png	1760000	f
51	Снегоход 2	6	111111	snow2.jpg	1250000	f
52	Снегоход 3	6	111111	snow3.jpg	560000	f
53	Снегоход 4	6	111111	snow4.jpg	1560000	f
54	Снегоход 5\n	6	111111	snow5.jpg	1320000	f
55	Снегоход 6	6	111111	snow6.png	1530000	f
56	Вездеход 1	7	111111	atv1.jpg	5760000	f
57	Вездеход 2	7	111111	atv2.jpg	4250000	f
58	Вездеход 3	7	111111	atv3.jpg	3560000	f
28	Гидроцикл 3	4	111111	jet3.png	560000	f
29	Гидроцикл 12	4	111111	jet12.png	1760000	f
30	Гидроцикл 11	4	111111	jet11.png	1110000	f
32	Гидроцикл 9	4	111111	jet9.png	1560000	f
33	Гидроцикл 8	4	111111	jet8.png	1650000	f
34	Гидроцикл 7	4	111111	jet7.png	1000000	f
35	Гидроцикл 6	4	111111	jet6.png	1530000	f
36	Гидроцикл 5\n	4	111111	jet5.png	1320000	f
37	Гидроцикл 4	4	111111	jet4.png	1560000	f
31	Гидроцикл 10	4	111111	jet10.jpg	1000000	f
14	Квадроцикл 2	3	111111	quad2.jpg	500000	f
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
12	okxolod2@gmail.com	Kzs5	2024-06-20	$argon2id$v=19$m=65536,t=3,p=4$lQnD44pbibziYN9A2Dc/+Q$KuL6fBU98MM3lKUuteJIZRKaFJLKuzrDRXhC9O3Gp4E	t	f	f	default_pfp.png
\.


--
-- TOC entry 3065 (class 0 OID 0)
-- Dependencies: 209
-- Name: AttributeValue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."AttributeValue_id_seq"', 392, true);


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

SELECT pg_catalog.setval('public."Products_id_seq"', 59, true);


--
-- TOC entry 3070 (class 0 OID 0)
-- Dependencies: 211
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 12, true);


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


-- Completed on 2024-07-02 22:35:49

--
-- PostgreSQL database dump complete
--

