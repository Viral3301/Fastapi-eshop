--
-- PostgreSQL database dump
--

-- Dumped from database version 13.12
-- Dumped by pg_dump version 13.12

-- Started on 2024-04-09 08:18:13

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
-- TOC entry 200 (class 1259 OID 16517)
-- Name: Accessories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Accessories" (
    id integer NOT NULL,
    title character varying NOT NULL,
    product_code integer,
    image character varying,
    price integer,
    manufacturer character varying(100),
    amount_in_stock integer,
    sale boolean,
    category integer,
    rating double precision,
    material character varying,
    guarantee integer,
    color character varying,
    company character varying
);


ALTER TABLE public."Accessories" OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16523)
-- Name: Accessories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Accessories_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Accessories_id_seq" OWNER TO postgres;

--
-- TOC entry 3077 (class 0 OID 0)
-- Dependencies: 201
-- Name: Accessories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Accessories_id_seq" OWNED BY public."Accessories".id;


--
-- TOC entry 202 (class 1259 OID 16525)
-- Name: Cart; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cart" (
    id integer NOT NULL,
    user_id integer,
    vehicle_id integer,
    accessory_id integer
);


ALTER TABLE public."Cart" OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16528)
-- Name: Cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Cart_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cart_id_seq" OWNER TO postgres;

--
-- TOC entry 3078 (class 0 OID 0)
-- Dependencies: 203
-- Name: Cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Cart_id_seq" OWNED BY public."Cart".id;


--
-- TOC entry 204 (class 1259 OID 16530)
-- Name: Category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Category" (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public."Category" OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16536)
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
-- TOC entry 3079 (class 0 OID 0)
-- Dependencies: 205
-- Name: Category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Category_id_seq" OWNED BY public."Category".id;


--
-- TOC entry 206 (class 1259 OID 16538)
-- Name: Orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Orders" (
    id integer NOT NULL,
    user_id integer,
    vehicle_id integer,
    accessory_id integer
);


ALTER TABLE public."Orders" OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16541)
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
-- TOC entry 3080 (class 0 OID 0)
-- Dependencies: 207
-- Name: Orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Orders_id_seq" OWNED BY public."Orders".id;


--
-- TOC entry 208 (class 1259 OID 16543)
-- Name: Users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Users" (
    id integer NOT NULL,
    email character varying NOT NULL,
    username character varying NOT NULL,
    registered_at date,
    hashed_password character varying NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_verified boolean NOT NULL,
    cart integer
);


ALTER TABLE public."Users" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16549)
-- Name: Users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Users_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Users_id_seq" OWNER TO postgres;

--
-- TOC entry 3081 (class 0 OID 0)
-- Dependencies: 209
-- Name: Users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Users_id_seq" OWNED BY public."Users".id;


--
-- TOC entry 210 (class 1259 OID 16551)
-- Name: Vehicles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Vehicles" (
    id integer NOT NULL,
    title character varying NOT NULL,
    product_code integer,
    image character varying,
    price integer,
    manufacturer character varying(100),
    seats integer,
    engine integer,
    engine_type character varying,
    year integer,
    amount_in_stock integer,
    sale boolean,
    category integer,
    rating double precision
);


ALTER TABLE public."Vehicles" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16557)
-- Name: Vehicles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Vehicles_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Vehicles_id_seq" OWNER TO postgres;

--
-- TOC entry 3082 (class 0 OID 0)
-- Dependencies: 211
-- Name: Vehicles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Vehicles_id_seq" OWNED BY public."Vehicles".id;


--
-- TOC entry 212 (class 1259 OID 16559)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16562)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying NOT NULL,
    username character varying NOT NULL,
    registered_at date,
    hashed_password character varying NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_verified boolean NOT NULL,
    image character varying
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16568)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO postgres;

--
-- TOC entry 3083 (class 0 OID 0)
-- Dependencies: 214
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- TOC entry 2895 (class 2604 OID 16570)
-- Name: Accessories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Accessories" ALTER COLUMN id SET DEFAULT nextval('public."Accessories_id_seq"'::regclass);


--
-- TOC entry 2896 (class 2604 OID 16571)
-- Name: Cart id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cart" ALTER COLUMN id SET DEFAULT nextval('public."Cart_id_seq"'::regclass);


--
-- TOC entry 2897 (class 2604 OID 16572)
-- Name: Category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Category" ALTER COLUMN id SET DEFAULT nextval('public."Category_id_seq"'::regclass);


--
-- TOC entry 2898 (class 2604 OID 16573)
-- Name: Orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders" ALTER COLUMN id SET DEFAULT nextval('public."Orders_id_seq"'::regclass);


--
-- TOC entry 2899 (class 2604 OID 16574)
-- Name: Users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Users" ALTER COLUMN id SET DEFAULT nextval('public."Users_id_seq"'::regclass);


--
-- TOC entry 2900 (class 2604 OID 16575)
-- Name: Vehicles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Vehicles" ALTER COLUMN id SET DEFAULT nextval('public."Vehicles_id_seq"'::regclass);


--
-- TOC entry 2901 (class 2604 OID 16576)
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- TOC entry 3057 (class 0 OID 16517)
-- Dependencies: 200
-- Data for Name: Accessories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Accessories" (id, title, product_code, image, price, manufacturer, amount_in_stock, sale, category, rating, material, guarantee, color, company) FROM stdin;
1	Рюкзак 1	111111	3609.345x0@2x.jpg	7500	Китай	2	f	1	4	Кордура	12	Красный	Grizzly
2	Рюкзак 2	111111	6318937169.jpg	9500	Китай	2	f	1	4	Флис	6	Черный	Lakestone
3	Рюкзак 3	111111	9517011631.jpg	12000	США	2	f	1	4	Кордура	12	Желтый	Lakestone
4	Рюкзак 4	111111	H015a123d640c42a89524946c48027f3cf.jpg	10000	Россия	2	f	1	4	Флис	12	Песочный	Bobby XD Design
5	Рюкзак 5	111111	sw-motech-Водонепроницаемый-рюкзак-baracuda-25-l..jpg	6500	Россия	2	f	1	4	Арамид	24	Серый	Grizzly
6	Гидрокостюм 1	111111	49568870299.jpg	8000	Россия	2	f	2	4	Неопрен	6	Черный	Bobby XD Design
7	Гидрокостюм 2	111111	49781580299.jpg	9750	Россия	3	f	2	5	Неопрен	12	Черный	Lakestone
8	Гидрокостюм 3	111111	65582970299.jpg	13000	США	1	f	2	3	Неопрен	24	Черный\n	Grizzly
9	Гидрокостюм 4	111111	af08f56__a830wb_01_sm-1-700x1404_1200.jpg	12500	Россия	1	f	2	4	Неопрен	6	Черный	Lakestone
10	Гидрокостюм 5	111111	H899d5960faed40eba1dac419bd01b28a.jpg	9000	Россия	1	t	2	4	Неопрен	6	Черный	Grizzly
\.


--
-- TOC entry 3059 (class 0 OID 16525)
-- Dependencies: 202
-- Data for Name: Cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cart" (id, user_id, vehicle_id, accessory_id) FROM stdin;
\.


--
-- TOC entry 3061 (class 0 OID 16530)
-- Dependencies: 204
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
-- TOC entry 3063 (class 0 OID 16538)
-- Dependencies: 206
-- Data for Name: Orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Orders" (id, user_id, vehicle_id, accessory_id) FROM stdin;
\.


--
-- TOC entry 3065 (class 0 OID 16543)
-- Dependencies: 208
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Users" (id, email, username, registered_at, hashed_password, is_active, is_superuser, is_verified, cart) FROM stdin;
\.


--
-- TOC entry 3067 (class 0 OID 16551)
-- Dependencies: 210
-- Data for Name: Vehicles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Vehicles" (id, title, product_code, image, price, manufacturer, seats, engine, engine_type, year, amount_in_stock, sale, category, rating) FROM stdin;
4	Квадроцикл 2	11111	7e52c442215b2f4dfbcae24f6358ba2d.png	475000	Китай	1	35	Двухтактный	2008	1	f	3	\N
5	Квадроцикл 3	11111	75lP3ut6Q08S57Cg9qWShCxgjONCCb5pDa73CLjl(600_400).png	500000	Китай	1	35	Двухтактный	2009	1	f	3	\N
6	Квадроцикл 4	11111	fj2cr9oo2ggqwu0cym47ihtqp6iv4bc0.png	500000	Китай	1	40	Двухтактный	2010	1	f	3	\N
7	Квадроцикл 5	11111	h6256662ecd664cc5ae1259de4aafbc7fo-kopia_623c45c17f8c3.jpg	600000	Россия	1	30	Двухтактный	2011	1	f	3	\N
8	Квадроцикл 6	11111	kvadrocikl3.jpg	560000	Россия	1	30	Двухтактный	2011	1	f	3	\N
9	Квадроцикл 7	11111	kvadrotsikl-yacota-slogger-1-1000x1000.jpg	350000	Россия	1	35	Двухтактный	2012	1	f	3	\N
10	Квадроцикл 8	11111	ORV-ATV-MY22-Can-Am-Outlander-MAX-XT-650-Oxford-Blue-SKU0002SNC00-34FR-NA.png	750000	США	1	40	Двухтактный	2019	1	f	3	\N
11	Квадроцикл 9	11111	overland-two-big-600x460.png	350000	США	1	40	Двухтактный	2013	1	f	3	\N
12	Квадроцикл 10	11111	pathmud.jpg	350000	Великобритания	1	40	Четырехтактный	2014	1	f	3	\N
13	Квадроцикл 11	11111	raptor-50n-zelenyj-kamuflyazh.jpg	650000	Великобритания	1	40	Четырехтактный	2017	1	f	3	\N
14	Квадроцикл 12	11111	Standart_max_0001_black-e02ad9e6-da77f03a.png	650000	Великобритания	1	40	Четырехтактный	2017	1	f	3	\N
15	Квадроцикл 13	11111	thumb_CFMOTO_CFORCE_520_EPS__8_.jpg	660000	Великобритания	1	40	Четырехтактный	2017	1	f	3	\N
16	Гидроцикл 1	11111	a49ea13c07f7389b698d81c2f2bfad06.png	2500000	Китай	2	250	Четырехтактный	2010	1	f	4	\N
17	Гидроцикл 2	11111	b66a5b20311e0945251e2a458ce86e5e.png	2450000	Китай	2	280	Четырехтактный	2012	1	f	4	\N
19	Гидроцикл 4	11111	jet.jpg	2750000	Китай	2	300	Четырехтактный	2014	1	f	4	\N
20	Гидроцикл 5	11111	noaudiosea-my23-rxp-x-ss-300-millenium-yellow-00021pj00-studio-34fr-na.png	2350000	США	2	300	Четырехтактный	2012	1	f	4	\N
21	Гидроцикл 6	11111	rxp-soundsystem-1.png	2820000	США	2	300	Четырехтактный	2012	1	f	4	\N
22	Гидроцикл 7	11111	rxt-260.png	2650000	США	2	300	Четырехтактный	2017	1	f	4	\N
24	Гидроцикл 9	11111	sea-my22-gtx-ltd-ss-300w-metallic-sage.png	1850000	Россия	2	300	Двухтактный	2010	1	f	4	\N
25	Гидроцикл 10	11111	SEA-MY22-WAKE-PRO-SS-230-Neo-Mint-SKU00013NC00-Studio-34FR-NA-500.png	2850000	Великобритания	2	300	Двухтактный	2018	1	f	4	\N
26	Гидроцикл 11	11111	sea-my23-spark-2up-base-229-manta-green-00061pa00-studio-34fr-na.png	2850000	Великобритания	2	300	Двухтактный	2018	1	f	4	\N
29	Гидроцикл 12	11111	7a7e24c762a4a6936573b6fe48b08ffd.png	2375000	Великобритания	2	300	Двухтактный	2018	1	f	4	\N
30	Катер 1	11111	6a9b3ca74a1da91cfd34d2beac8dbff1.png	2747000	Китай	2	150	Четырехтактный	2010	1	t	5	\N
31	Катер 2	11111	106c66ca89e137d8128e7b53250671ac.png	3500000	Китай	2	180	Четырехтактный	2015	1	f	5	\N
32	Катер 3	11111	b3ab386ed04a.jpg	2500000	Китай	2	180	Четырехтактный	2018	1	f	5	\N
33	Катер 4	11111	bez_imeni_1_0049_fon_0002_gel_tricked_out_vosstanovleno_vosstanovleno_0005_26lsv_top_0010_bez_imeni_1_0049_fon_0002_gel_.jpg	2700000	Китай	2	180	Четырехтактный	2018	1	f	5	\N
34	Катер 5	11111	bez-imeni_1_0049_fon_0002_gel_tricked_out_vosstanovleno_vosstanovleno.jpg_0000_malibu-_53_.jpg	3200000	Россия	2	200	Четырехтактный	2020	1	f	5	\N
35	Катер 6	11111	bez-imeni_1_0049_fon_0002_gel_tricked_out_vosstanovleno_vosstanovleno.jpg_0002_malibu-_2_.jpg	3300000	Россия	2	150	Четырехтактный	2017	1	f	5	\N
36	Катер 7	11111	bez-imeni_1_0049_fon_0002_gel_tricked_out_vosstanovleno-kopiya-2.jpg	2750000	Великобритания	2	150	Четырехтактный	2017	1	t	5	\N
37	Катер 8	11111	c88f89902fd0c17db466ec8a67224d3a.jpg	4000000	Великобритания	2	150	Четырехтактный	2021	1	f	5	\N
38	Катер 9	11111	ce35540c2d75.jpg	3000000	США	2	200	Четырехтактный	2020	1	f	5	\N
39	Катер 10	11111	images.jpg	3200000	США	2	200	Четырехтактный	2020	1	f	5	\N
40	Катер 11	11111	t220_bow.png	2800000	США	2	170	Четырехтактный	2010	1	t	5	\N
41	Катер 12	11111	t250_front_bow.png	2500000	США	2	190	Четырехтактный	2012	1	t	5	\N
42	Снегоход 1	11111	dpyr7tac2yv7b18g8rnaid48z0bvof2e.png	240000	Китай	1	125	Двухтактный	2009	1	f	6	\N
43	Снегоход 2	11111	f6978208f6fe8318aad64cfd4026aa4d.jpg	340000	Китай	1	150	Двухтактный	2015	1	f	6	\N
44	Снегоход 3	11111	snegokhod-polaris-850-rmk-khaos-155-3-1_5eb461dfe0a68.png	450000	Китай	1	150	Четырехтактный	2018	1	f	6	\N
45	Снегоход 4	11111	stels-ataman-sa800t-1.jpg	250000	США	1	160	Четырехтактный	2018	1	t	6	\N
46	Снегоход 5	11111	stels-ataman-sa-800-t-foto-01.jpg	250000	США	1	160	Четырехтактный	2018	1	t	6	\N
47	Снегоход 6	11111	stels-ataman-sa-800-t-foto-03.jpg	350000	Россия	1	160	Четырехтактный	2018	1	f	6	\N
48	Вездеход 1	11111	1200x640-2k.jpg	6500000	Китай	6	146	Дизельный	2019	1	t	7	\N
18	Гидроцикл 3	11111	gidrotsikl-brp-seadoo-rxt-300x-ibr-2019-2_5eb46fbb98845.png	2450000	Китай	2	280	Четырехтактный	2014	1	f	4	\N
49	Вездеход 2	11111	1200x640-3m.jpg	10000000	Россия	6	146	Дизельный	2019	1	f	7	\N
50	Вездеход 3	11111	1200x640-4w.jpg	9000000	Россия	6	146	Дизельный	2019	1	f	7	\N
23	Гидроцикл 8	11111	SEA-MY21-REC-GTI-SE-170-SS-Neo-Yellow-Ice-Metal-34FRT-LR_result-1.png	2150000	Россия	2	300	Четырехтактный	2013	1	f	4	1
1	Квадроцикл 1	11111	1_63db50219a66c.png	1	Китай	1	40	Двухтактный	2007	2	f	3	\N
\.


--
-- TOC entry 3069 (class 0 OID 16559)
-- Dependencies: 212
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
05b859e0eb12
\.


--
-- TOC entry 3070 (class 0 OID 16562)
-- Dependencies: 213
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, email, username, registered_at, hashed_password, is_active, is_superuser, is_verified, image) FROM stdin;
12	okxolod2@gmail.com	xolod	2023-07-11	$2b$12$Co/h2NYZeMlPu4/ioKzOlOACd9mTbwmX5CR3NoZhPyChvmUCLs3XC	t	f	f	imageeee.jpg
22	email@bb.ru	sdda	2023-08-05	$2b$12$vgBICmE9NnfEH0KuRU.9K.YL4BmK7dfJ1L1qHxDOrSbLFP.PJKq2W	t	f	f	default_pfp.png
13	asda	xolod2	2023-07-11	$2b$12$9/RyapfueD7/QuNG4eUUXOBJ0HVDV8hIK91Mm4Yux6ygMcG0SRWdK	t	f	f	default_pfp.png
14	email@bk.ru	hello	2023-07-13	$2b$12$cQb9EjacHDg1tvitBFqQz.YyPsqNamKRHOi8lWSYm8pSpVHjUq5V2	t	f	f	default_pfp.png
15	string	string	2023-07-13	$2b$12$5RIXI3avXnmFOoRoGDrSQ.fHmSBcWHCdAa30RplzZx3.FBmDf87N.	t	f	f	default_pfp.png
16	string2	string2	2023-07-13	$2b$12$FWYt8fBtiKCPXDh4Bshih.lM.7XGjTyCM.qTDyOanCsKN/uolJAKK	t	f	f	default_pfp.png
17	string3	string3	2023-07-13	$2b$12$dPAc/kcpbT.GkYnmUybJf.fZTFtdGEnSTCkval702UkDrUtA1J6jW	t	f	f	default_pfp.png
18	test	test	2023-07-17	$2b$12$FtJ1KvmEjX2me9M6q7Nqi.YV.I0FzivRHP0IK/TE45nNLk37JPn2O	t	f	f	default_pfp.png
19	XY@mail.com	Xolod	2023-07-17	$2b$12$/YHgogNAnp0cjOxYEXfPXONpnjNcXAQrUn.JzHFB8Lc0jB0RmywcW	t	f	f	default_pfp.png
20	22@bk.ru	asdas	2023-07-17	$2b$12$wq87N1bpW84pfkNw62BpS.PAvvUZrQSItNoZhPzIe9tfNE1Pg8jEm	t	f	f	default_pfp.png
21			2023-07-17	$2b$12$Lt9HYu.VRXmilp4BsiFMtOjT6w0vfsW.bUQEQpGjU6Bw2xi9ikHiC	t	f	f	default_pfp.png
23	testemail@bk.ru	testtt	2023-11-15	$2b$12$CSyRAUv1/6MmQBDKBd2ZA.OTz8.h5Vv5kKLxQhfF5UFORsmkSeBoi	t	f	f	default_pfp.png
24	okxolod232322@gmail.com	Xolod	\N	$2b$12$YJzmZ.5lXpezC4aINJVy6.OHmRYAD8gnzlx/m.owvzatPzWX7sJIe	t	f	f	default.pfp
\.


--
-- TOC entry 3084 (class 0 OID 0)
-- Dependencies: 201
-- Name: Accessories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Accessories_id_seq"', 20, true);


--
-- TOC entry 3085 (class 0 OID 0)
-- Dependencies: 203
-- Name: Cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cart_id_seq"', 1, false);


--
-- TOC entry 3086 (class 0 OID 0)
-- Dependencies: 205
-- Name: Category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Category_id_seq"', 9, true);


--
-- TOC entry 3087 (class 0 OID 0)
-- Dependencies: 207
-- Name: Orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Orders_id_seq"', 1, false);


--
-- TOC entry 3088 (class 0 OID 0)
-- Dependencies: 209
-- Name: Users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Users_id_seq"', 1, false);


--
-- TOC entry 3089 (class 0 OID 0)
-- Dependencies: 211
-- Name: Vehicles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Vehicles_id_seq"', 51, true);


--
-- TOC entry 3090 (class 0 OID 0)
-- Dependencies: 214
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 24, true);


-- Completed on 2024-04-09 08:18:13

--
-- PostgreSQL database dump complete
--

