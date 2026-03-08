create table sangdata(
code int primary key,
sang varchar(20),
su int,
dan int);

insert into sangdata values(1,'장갑',3,10000);
insert into sangdata values(2,'벙어리장갑',2,12000);
insert into sangdata values(3,'가죽장갑',10,50000);
insert into sangdata values(4,'가죽점퍼',5,650000);

SELECT * FROM sangdata;
DESC sangdata;


create table buser(
buserno int primary key, 
busername varchar(10) not null,
buserloc varchar(10),
busertel varchar(15));

insert into buser values(10,'총무부','서울','02-100-1111');
insert into buser values(20,'영업부','서울','02-100-2222');
insert into buser values(30,'전산부','서울','02-100-3333');
insert into buser values(40,'관리부','인천','032-200-4444');

SELECT * FROM buser;
DESC buser;

create table jikwon(
jikwonno int primary key,
jikwonname varchar(10) not null,
busernum int not null,
jikwonjik varchar(10) default '사원', 
jikwonpay int,
jikwonibsail date,
jikwongen varchar(4),
jikwonrating char(3),
CONSTRAINT ck_jikwongen check(jikwongen='남' or jikwongen='여'));

insert into jikwon values(1,'홍길동',10,'이사',9900,'2008-09-01','남','a');
insert into jikwon values(2,'한송이',20,'부장',8800,'2010-01-03','여','b');
insert into jikwon values(3,'이순신',20,'과장',7900,'2010-03-03','남','b');
insert into jikwon values(4,'이미라',30,'대리',4500,'2014-01-04','여','b');
insert into jikwon values(5,'이순라',20,'사원',3000,'2017-08-05','여','b');
insert into jikwon values(6,'김이화',20,'사원',2950,'2019-08-05','여','c');
insert into jikwon values(7,'김부만',40,'부장',8600,'2009-01-05','남','a');
insert into jikwon values(8,'김기만',20,'과장',7800,'2011-01-03','남','a');
insert into jikwon values(9,'채송화',30,'대리',5000,'2013-03-02','여','a');
insert into jikwon values(10,'박치기',10,'사원',3700,'2016-11-02','남','a');
insert into jikwon values(11,'김부해',30,'사원',3900,'2016-03-06','남','a');
insert into jikwon values(12,'박별나',40,'과장',7200,'2011-03-05','여','b');
insert into jikwon values(13,'박명화',10,'대리',4900,'2013-05-11','남','a');
insert into jikwon values(14,'박궁화',40,'사원',3400,'2016-01-15','여','b');
insert into jikwon values(15,'채미리',20,'사원',4000,'2016-11-03','여','a');
insert into jikwon values(16,'이유가',20,'사원',3000,'2016-02-01','여','c');
insert into jikwon values(17,'한국인',10,'부장',8000,'2006-01-13','남','c');
insert into jikwon values(18,'이순기',30,'과장',7800,'2011-11-03','남','a');
insert into jikwon values(19,'이유라',30,'대리',5500,'2014-03-04','여','a');
insert into jikwon values(20,'김유라',20,'사원',2900,'2019-12-05','여','b');
insert into jikwon values(21,'장비',20,'사원',2950,'2019-08-05','남','b');
insert into jikwon values(22,'김기욱',40,'대리',5850,'2013-02-05','남','a');
insert into jikwon values(23,'김기만',30,'과장',6600,'2015-01-09','남','a');
insert into jikwon values(24,'유비',20,'대리',4500,'2014-03-02','남','b');
insert into jikwon values(25,'박혁기',10,'사원',3800,'2016-11-02','남','a');
insert into jikwon values(26,'김나라',10,'사원',3500,'2016-06-06','남','b');
insert into jikwon values(27,'박하나',20,'과장',5900,'2012-06-05','여','c');
insert into jikwon values(28,'박명화',20,'대리',5200,'2013-06-01','여','a');
insert into jikwon values(29,'박가희',10,'사원',4100,'2016-08-05','여','a');
insert into jikwon values(30,'최미숙',30,'사원',4000,'2015-08-03','여','b');

SELECT * FROM jikwon;
DESC jikwon;



create table gogek(
gogekno int primary key,
gogekname varchar(10) not null,
gogektel varchar(20),
gogekjumin char(14),
gogekdamsano int,
CONSTRAINT FK_gogekdamsano foreign key(gogekdamsano) references jikwon(jikwonno));

insert into gogek values(1,'이나라','02-535-2580','850612-1156777',5);
insert into gogek values(2,'김혜순','02-375-6946','700101-1054777',3);
insert into gogek values(3,'최부자','02-692-8926','890305-1065777',3);
insert into gogek values(4,'김해자','032-393-6277','770412-2028777',13);
insert into gogek values(5,'차일호','02-294-2946','790509-1062777',2);
insert into gogek values(6,'박상운','032-631-1204','790623-1023777',6);
insert into gogek values(7,'이분','02-546-2372','880323-2558777',2);
insert into gogek values(8,'신영래','031-948-0283','790908-1063777',5);
insert into gogek values(9,'장도리','02-496-1204','870206-2063777',4);
insert into gogek values(10,'강나루','032-341-2867','780301-1070777',12);
insert into gogek values(11,'이영희','02-195-1764','810103-2070777',3);
insert into gogek values(12,'이소리','02-296-1066','810609-2046777',9);
insert into gogek values(13,'배용중','02-691-7692','820920-1052777',1);
insert into gogek values(14,'김현주','031-167-1884','800128-2062777',11);
insert into gogek values(15,'송운하','02-887-9344','830301-2013777',2);


SELECT * FROM gogek;

DESC gogek;

--select : db 서버로부터 클라이언트로 자료를 읽는 명령
--select 칼럼명 as 별명, ... from 테이블 명 where 조건 order by 기준키, ...

SELECT * FROM jikwon;
SELECT jikwonno, jikwonname FROM jikwon;					--2개만 읽은거임(selection)
SELECT jikwonno, jikwongen, busernum, jikwonname FROM jikwon WHERE jikwongen = '여';
SELECT jikwonno AS 직원번호, jikwonname as 직원명 FROM jikwon;

SELECT 10, '안녕', 12/3 as 결과 FRom dual;							--가상 테이블을 이용해서 만들어본 것

SELECT jikwonname, jikwonpay, jikwonpay * 0.05 as tax FROM jikwon;
SELECT jikwonname, CONCAT(jikwonname, '님') As jikwonetc FROm jikwon;

--정렬(sort)
SELECT * FROM jikwon ORDER BY jikwonpay ASC;
SELECT * FROM jikwon ORDER BY jikwonpay;
SELECT * FROM jikwon ORDER BY jikwonpay DESC;
SELECT * FROM jikwon ORDER BY jikwonjik ASC;
SELECT * FROM jikwon ORDER BY jikwonjik ASC, busernum DESC, jikwongen ASC, jikwonpay;
SELECT jikwonname, jikwonpay, jikwonpay/100 AS pay FROM jikwon ORDER BY pay DESC;



--중복 배제
SELECT DISTINCT jikwonjik FROM jikwon;
--이렇게 쓰면 안된다.
--SELECT DISTINCT jikwonjik, jikwonname FROM jikwon;


--연산자 : () > 산술(*, /, +, -) > 관계(비교) > is null, like, in > between, not > and > or
SELECT * FROM jikwon WHERE jikwonjik = '대리';				--레코드 선택
SELECT * FROM jikwon WHERE jikwonno = 3;
SELECT * FROM jikwon WHERE jikwonibsail = '2010-03-03';
SELECT * FROM jikwon WHERE jikwonno = 5 OR jikwonno = 7;
SELECT * FROM jikwon WHERE jikwonjik = '사원' And jikwongen = '여';
SELECT * FROM jikwon WHERE jikwonjik = '사원' And jikwongen = '여' and jikwonpay <= 3000;
SELECT * FROM jikwon WHERE jikwonjik = '사원' ANd (jikwongen = '여' or jikwonibsail <= 2017-01-01);


SELECT * FROM jikwon WHERE jikwonno >= 5 AND jikwonno <= 10;
SELECT * FROM jikwon WHERE jikwonno BETWEEN 5 AND 10;
SELECT * FROM jikwon WHERE jikwonibsail BETWEEN '2017-1-1' AND '2019-12-31';

SELECT * FROM jikwon WHERE jikwonno < 5 OR jikwonno > 10;
SELECT * FROM jikwon WHERE jikwonno not BETWEEN 5 AND 20;			--긍정적 형태의 조건이 속도를 향상시킨다.

SELECT * FROM jikwon WHERE jikwonpay > 5000;
SELECT * FROM jikwon WHERE jikwonpay > 3000 + 2000;

SELECT * FROM jikwon WHERE jikwonname = '홍길동';
SELECT * FROM jikwon WHERE jikwonname >= '박';							--사전에서 뒤질 때 '박' 이후의 사람들

SELECT ASCII('a'), ASCII('A'), ASCII('가'), ASCIi('나') FROM dual;									--아스키코드를 확인해 본다.


SELECT * FROM jikwon WHERE jikwonname BETWEEN '김' ANd '박';  		--박씨 전까지만 나온다


--in 멤버 조건 연산
SELECT * FROM jikwon WHERE jikwonjik = '대리' or jikwonjik = '과장' or jikwonjik = '부장';
SELECT * FROM jikwon WHERE jikwonjik IN ('대리', '과장', '부장');

--like 조건 연산: %(0개 이상의 문자열), _(한개 문자)
SELECT * FROM jikwon WHERE jikwonname LIKE '이%';
SELECT * FROM jikwon WHERE jikwonname LIKE '이순%';
SELECT * FROM jikwon WHERE jikwonname LIKE '%라';							--마지막 글자가 '라'
SELECT * FROM jikwon WHERE jikwonname LIKE '이%라';						--첫글자가 '이' 마지막 글자가 '라' 가운데는 아무거나

SELECT * FROM jikwon WHERE jikwonname LIKE '이__';							--'이'로 시작하며 최대 글자가 3글자
SELECT * FROM jikwon WHERE jikwonname LIKE '이_라';

SELECT * FROM jikwon WHERE jikwonname LIKE '__';							--이름이 두글자인 사람들
SELECT * FROM jikwon WHERE jikwonpay LIKE '3___';							--연봉이 3천대인 사람들
SELECT * FROM jikwon WHERE jikwonpay LIKE '3%';								--연봉이 3으로 시작하는 사람들


SELECT * FROM gogek;
SELECT * FROM gogek WHERE gogekjumin LIKE '_______1%';
SELECT * FROM gogek WHERE gogekjumin LIKE '%-1%';


SELECT * FROM jikwon;

UPDATE jikwon SET jikwonjik = NULL WHERE jikwonno = 5;
--SELECT * FROM jikwon WHERE jikwonjik = NULL; --XX이건 안됨
SELECT * FROM jikwon WHERE jikwonjik IS NULL;

SELECT * FROM jikwon LIMIT 3;
SELECT * FROM jikwon order BY jikwonno DESC LIMIT 3;
SELECT * FROM jikwon LIMIT 5,3;				--(시작행, 갯수)


SELECT jikwonno AS 직원번호, jikwonname as 직원명, jikwonjik As 직급, jikwonpay as 연봉,
jikwonpay / 12 AS 보너스, jikwonibsail as 입사일 from jikwon
WHERE jikwon IN ('과장', '부장','사원') and jikwonpay >= 4000 and jikwonibsail Between '2015-1-1' and '2019-12-31'
ORDER BY jikwonjik, jikwonpay DESC LIMIT 3;

--내장함수 : 데이터 조작의 효율성 증진이 목적
--단일행 함수: 각 행에 대해 작업한다. 행단위 처리
--문자함수

SELECT LOWER('Hello'), UPPER('Hello') FROM dual;
SELECT SUBSTRING('hello world', 3),SUBSTRING('hello world', 3, 3),
SUBSTRING('hello world', -3, 3) FROM dual;

SELECT LENGTH('hello world'), INSTR('hello world', 'e') FROM dual;
SELECT REPLACE('010.111.1234', '.', '-') FROM dual;
--...

--jikwon 테이블에서 이름에 '이'가 포함된 직원이 있으면 '이'부터 두글자 출력하기
SELECT jikwonname, SUBSTRING(jikwonname, INSTR(jikwonname,'이'),2)
FROM jikwon WHERE jikwonname LIKE '%이%';




--숫자함수
SELECT ROUND(45.678,2), ROUND(45.678), ROUND(45.678,0), ROUND(45.678,-1) FROM dual;
SELECT jikwonname, jikwonpay, jikwonpay * 0.25 AS tax , ROUND(jikwonpay * 0.25, 0) FROM jikwon;


SELECT TRUNCATE(45.678,0), TRUNCATE(45.678,1), TRUNCATE(45.678,-1) FROM dual;
SELECT MOD(15/2), 15/2 FROM dual;
SELECT GREATEST(23,25,5,1,12), LEAST(23,25,5,1,12) FROM dual;


--날짜함수
SELECT NOW(), NOW() + 2, SYSDATE(), CURDATE() FROM dual;
SELECT NOW(), SLEEP(3), NOW() FROM dual;							--하나의 query 내에서는 동일 값 출력
SELECT SYSDATE(), sleep(3), SYSDATE() FROM dual;				--실행 시점값 출력
SELECT ADDDATE('2020-08-01', 3),ADDDATE('2020-08-01', -3), SUBDATE('2020-08-01', 3)	--날짜 더하고 빼기, 윤년체크


SELECT DATE_ADD(NOW(), INTERVAL 1 MINUTE), 
DATE_ADD(NOW(), INTERVAL 5 DAY), 
DATE_ADD(NOW(), INTERVAL 5 MONTH) FROM dual;

SELECT datediff(NOW(), '2025-05-05');

--...

--형변환 함수
SELECT now(), date_format(NOW(), '%Y%m%d'), date_format(NOW(), '%Y년%m월%d일');
SELECT jikwonname, jikwonibsail, DATE_FORMAT(jikownibsail,'%W')
FROM jikwon WHERE busernum = 10;

SELECT str_to_date('2026-02-12:16', '%Y-%m-%d');
SELECT str_to_date('2026-02-12 16:13:34', '%Y-%m-%d %H:%i:%S');


--기타 함수
--rank() : 순위 결정
SELECT jikwonno, jikwonname, jikwonpay, 
rank() over(ORDER BY jikwonpay DESC) 
FROM jikwon;


SELECT jikwonno, jikwonname, jikwonpay, 
rank() over(ORDER BY jikwonpay) AS result,
dense_rank() over(ORDER BY jikwonpay) AS reusult2
FROM jikwon;

--dense rank와 rank의 차이는 동점자가 나왔을 때 rank는 1, 1, 3이고 dense rank는 1, 1, 2
--nvl(value1, value2) : value1이 null이면 value2를 취한다.
SELECT jikwonname, jikwonjik, nvl(jikwonjik,'임시직')
FROM jikwon;

--nvl2(value1, value2, value3) : value1이 null인지 판단한 뒤 null이면 value2를 아니면 value3을 취한다.
SELECT jikwonname, jikwonjik, nvl2(jikwonjik,'정규직', '임시직')
FROM jikwon;

--nullif(value1, value2): 두개의 값이 일치하면 null, 아니면 value1 취함
SELECT jikwonname, jikwonjik, NULLIF(jikwonjik, '대리') FRom jikwon;


--조건 표현식
--형식 1) case 표현식 when  비교값1 then 결과값1 when 비교값1 then 결과값2 ...[else 결과값n] end as 별명
SELECT CASE 10/5 
WHEN 5 THEN '안녕'
WHEN 2 THen '반가워' 
else '잘가' end as 결과 from dual;

SELECT jikwonname, jikwonpay, jikwonjik,
CASE jikwonjik
WHEN '이사' THen jikwonpay * 0.05
WHEN '부장' THen jikwonpay * 0.04
WHEN '부장' THen jikwonpay * 0.03
ELSE jikwonpay * 0.02 END donation FROM jikwon;

--형식 2) case when 조건1 then 결과값1 when 조건2 then 결과값2 ...[else 결과값n] end as 별명
SELECT jikwonname, 
CASE WHEN jikwongen='남' THEn '남성' 
When jikwongen='여' then '여성' 
End as gender FROM jikwon;

SELECT jikwonname, jikwonpay,
CASE
WHEN jikwonpay >= 7000 THEN '우수연봉'
WHEN jikwonpay >= 5000 THEN '보통연봉'
ELSE '저조' End as result FRom jikwon WHEre jikwonjik In ('대리', '과장');

--if(조건) 참값, 거짓값 as 별명
SELECT jikwonname, jikwonpay, jikwonjik, 
TRUNCATE(jikwonpay/1000,0) FROM jikwon;


SELECT jikwonname, jikwonpay, jikwonjik, 
IF(TRUNCATE(jikwonpay/1000,0)>=5, 'good', 'normal') AS result FROM jikwon;



SELECT
jikwonname AS 직원명,
DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') AS 근무년수,
CASE
	WHEN DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') >= 10
		THEN '감사합니다'
	ELSE '열심히' END AS 표현,
CASE
	WHEN DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') >= 5
		THEN truncate(jikwonpay * 0.05,0)
	ELSE 0 END AS 특별수당
FROM jikwon WHERE DATE_FORMAT(jikwonibsail, '%Y')>=2010;


SELECT
jikwonname AS 직원명, jikwonjik as 직급, DATE_FOrmat(jikwonibsail, '%Y.%m.%d') as 입사년월일,
case
	when datediff(NOW(), jikwonibsail) >= 8 * 365
		THEN '왕고참'
   WHEN datediff(NOW(), jikwonibsail) >= 5 * 365
   	then '고참'
   WHEN datediff(NOW(), jikwonibsail) >= 3 *365
   	then '보통'
   ELSE '일반' End as 구분,
CASE
	when busernum = 10 Then '총무부'
   when busernum = 20 Then '영업부'
   when busernum = 30 Then '전산부'
   when busernum = 40 Then '관리부'
   end AS 부서 
FROM jikwon;



SELECT 
jikwonno AS 사번, jikwonname as 직원명, busernum AS 부서, jikwonpay as 연봉,
CASE
	WHEN busernum = 10 
		then truncate(jikwonpay * 1.1,0)
   WHEN busernum = 30
   	then truncate(jikwonpay * 1.2,0)
   ELSE jikwonpay END AS 인상연봉,
CASE
	when datediff(NOW(), jikwonibsail) >= 15 * 365
		THEN 'O'
   ELSE 'X' END AS 장기근속
FROM jikwon;
   

 
--집계함수(복수행 함수) : 전체 자료를 그룹별로 구분해 통계 결과를 얻기 위한 함수
SELECT sum(jikwonpay) AS 합, AVg(jikwonpay) As 평균, max(jikwonpay) as 최대, min(jikwonpay) as 최소 FROM jikwon;

 
SELECT * FROM jikwon;
UPDATE jikwon SET jikwonpay = NULL WHERE jikwonno=5; 
DESC jikwon;
 
SELECT AVG(jikwonpay), AVG(nvl(jikwonpay,0)) FROM jikwon; 
--29명으로 나누고 30으로 나눈다. 집계함수는 null은 작업에서 제외하고 처리하기 때문에 포함하고 싶으면 뒤에 방법 사용

SELECT sum(jikwonpay)/29, sum(jikwonpay)/30 FROM jikwon;

SELECT sum(jikwonpay), sum(jikwonpay) FROM jikwon;			--sum은 똑같다

SELECT COUNT(jikwonno), COUNT(jikwonpay), COUNT(jikwonjik) FROM jikwon;
SELECT COUNT(*) AS 인원수 From jikwon;			--건수 구할때는 *로 해라 어디에 null 숨어있을지 모르니까

SELECT STDDEV(jikwonpay) AS 표준편차, var_samp(jikwonpay) AS 분산 FROM jikwon;		--표준편차와 분산
SELECT COUNT(*) AS 인원, var_samp(jikwonpay) as 분산 From jikwon Where busernum=10;		
SELECT COUNT(*) AS 인원, var_samp(jikwonpay) as 분산 From jikwon Where busernum=20;		
