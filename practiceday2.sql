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


--day4  
--과장은 몇명인가
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonjik = '과장';


--2010년 이전에 입사한 남직원은 몇명?
SELECT COUNT(*) AS 인원수 From jikwon WHere jikwonibsail < '2010-1-1' and jikwongen='남';

--2015년 이후 입사한 여직원의 연봉합, 연봉평균, 인원수는?
SELECT SUM(jikwonpay) AS 연봉합, avg(jikwonpay) AS 연봉평균, count(*) AS 인원수
from jikwon WHERE jikwonibsail>'2015-1-1' AND jikwongen='여' ;

--그룹함수 : group by 절 : 소계 출력
--SELECT 그룹칼럼명, 계산함수, ...from 테이블명 where 조건 group by 그룹칼럼명 having  출력조건
--그룹칼럼에 대해 order by 할 수 없다. 단, 출력 결과는 order by 가능

--성별 연봉 평균, 인원수 출력
SELECT jikwongen, AVG(jikwonpay), COUNT(*) FROM jikwon GROUP BY jikwongen;

--부서별 연봉합
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

--부서별 연봉합 : 연봉합이 35000 이상
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;

--부서별 연봉합 : 여성만
SELECT busernum, SUM(jikwonpay) FROM jikwon WHERE jikwongen = '여' GROUP BY busernum;

--부서별 연봉합 : 연봉합이 15000 이상인 여성만
SELECT busernum, SUM(jikwonpay) FROM jikwon WHERE jikwongen = '여' GROUp By busernum HAVINg SUm(jikwonpay) >= 15000;

SELECT busernum, SUM(jikwonpay) AS paytotal FROM jikwon WHERE jikwongen = '여' GROUp By busernum HAVINg paytotal >= 15000;

--주의
--SELECT busernum, SUM(jikwonpay) FROM jikwon order by busernum GROUP BY busernum;			syntax 	error
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum ORDER BY SUM(jikwonpay) DESC;		--이건 가능(결과에 대한 정렬)


--문제 풀이
SELECT jikwonjik, AVG(nvl(jikwonpay,0)) as 급여평균 from jikwon GROUp by jikwonjik;
SELECT jikwonjik, AVG(jikwonpay) as 급여평균 from jikwon Where jikwonjik IS not null GROUp by jikwonjik;

SELECT jikwonjik, AVG(nvl(jikwonpay,0)) AS 급여평균 from jikwon Where jikwonjik='부장' or jikwonjik='과장' GROUp by jikwonjik;

SELECT date_format(jikwonibsail,'%Y') AS 입사년도, COUNT(*) AS 직원수 From jikwon WHere DATE_FORmat(jikwonibsail, '%Y')<2015 GROUP by 입사년도;

SELECT nvl(jikwonjik, '임시직') AS 직급, jikwongen AS 성별, count(*) AS 인원수, Sum(jikwonpay) as 급여합 from jikwon GROUP BY 직급,성별;

SELECT busernum AS 부서번호, sum(jikwonpay) as 급여합 FROM jikwon where busernum = 10 or busernum = 20 group by 부서번호;

SELECT jikwonjik AS 직급, Sum(jikwonpay) as 급여의총합 FROM jikwon Group By 직급 having 급여의총합 >= 7000;

SELECT nvl(jikwonjik, '임시직') AS 직급, COUNT(*) as 인원수, sum(jikwonpay) from jikwon GROUP BY 직급 HAVING 인원수 >= 3; 

--여러개의 테이블이 있으면 2개씩 조인해서 늘려가야한다.
--join !! : 하나 이상의 테이블에서 원하는 자료 추출
--반드시 공통칼러밍 필요하다.

DESC buser;
DESC jikwon;
DESC gogek;
INSERT INTO buser(buserno, busername) VALUES(50, '기획실')

SELECT * FROM jikwon;



ALTER TABLE jikwon MODIFY busernum INT NULL;
UPDATE jikwon SET busernum=NULL WHERE jikwonno = 5;
SELECT * FROM jikwon;


SELECT test.jikwon.jikwonname FROM jikwon;
SELECT mytab.jikwonname FROM jikwon AS mytab;		--table에 별명을 줄 수 있다.


--corss join : 한쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 조인하는 기능
SELECT jikwonname, busername FROM jikwon, buser;
SELECT jikwonname, busername FROM jikwon CROSS JOIN buser;					--ANSI 표준 SQL


--cross join 중 self join
SELECT a.jikwonname, b.jikwonname FROM jikwon a, jikwon b;

--EQUI join : join 조건식에 '='을 사용. 두 테이블은 '같다' 조건으로 join
--대부분의 pk-fk 조인은 EQUI join 이다.
SELECT jikwonname, busername FROM jikwon, buser
WHERE jikwon.busernum = buser.buserno;

--non-EQUI join : 조인 조건식에 '=' 이외의 관계연산자를 사용
CREATE TABLE paygrade(grade INT PRIMARY KEY, lpay INT, hpay INT);
INSERT INTO paygrade VALUES(1, 0, 1999);
INSERT INTO paygrade VALUES(2, 2000, 2999);
INSERT INTO paygrade VALUES(3, 3000, 3999);
INSERT INTO paygrade VALUES(4, 4000, 4999);
INSERT INTO paygrade VALUES(5, 5000, 9999);

SELECT * FROM paygrade;

SELECT jiktab.jikwonname, jiktab.jikwonpay, paytab.grade 
FROM jikwon AS jiktab, paygrade AS paytab
WHERE jiktab.jikwonpay >= paytab.lpay AND jiktab.jikwonpay <= paytab.hpay;


--inner join : 두 테이블을 조인할 때, 두 페이블에 모두 지정한 열의 데이터가 있는 경우만 추출
SELECT jtab.jikwonno, jtab.ikwonname, btab.busername FROM jikwon AS jtab, buser AS btab
WHERE jtab.busernum = btab.buserno;			--oracle엣 주로 사용

SELECT jikwonno, jikwonname, busername FROM jikwon, buser
WHERE busernum = buserno;	

SELECT jikwonno, jikwonname, busername FROM jikwon, buser
WHERE busernum = buserno AND jikwongen = '남';				--where 조건에 join 조건 + record 제한 조건 -가독성 나쁨 




SELECT jikwonno, jikwonname, busername FROM jikwon INNER JOIN buser ON busernum = buserno;


SELECT jikwonno, jikwonname, busername 
FROM jikwon INNER JOIN buser ON busernum = buserno 	--	join 조건은 on으로 걸기 ANSI
WHERE jikwongen='남';						--record 제한 조건은 where로 걸기


--outer join : 두 테이블을 조인할 때 1개의 테이블에만 자료가 있어도 결과 추출
--left outer join
--SELECT jikwonno, jikwonname, busername FROM jikwon, buser
--WHERE busernum = buserno(+);				--oracle용: MariaDB X  대응안된 것들은 null을 허용 왼쪽은 다 나오고 오른쪽은 null이 나올수 있음

--SELECT jikwonno, jikwonname, busername FROM jikwon, buser
--WHERE busernum(+) = buserno;				--oracle용 오른쪽은 다 나오지만 왼쪽은 null 허용


--left outer join
SELECT jikwonno, jikwonname, busername
FROM jikwon LEFT OUTER JOIN buser
ON busernum=buserno;

--right outer join
SELECT jikwonno, jikwonname, busername
FROM jikwon RIGHT OUTER JOIN buser
ON busernum=buserno;

--full outer join											oracle에서만 지원
--SELECT jikwonno, jikwonname, busername
--FROM jikwon FULL OUTER JOIN buser
--ON busernum=buserno;



--MariaDB의 full outer join은 union을 이용
SELECT jikwonno, jikwonname, busername FROM jikwon LEFT OUTER JOIN buser ON busernum=buserno
UNION
SELECT jikwonno, jikwonname, busername FROM jikwon right OUTER JOIN buser ON busernum=buserno;




SELECT jikwonno AS 직원번호, jikwonname as 직원명, busername AS 부서명
FROM jikwon INNER JOIN buser ON busernum = buserno
WHERE jikwongen='남' ANd jikwonname LIKe '김%';

SELECT SUM(jikwonpay) AS hap, COUNT(*) AS COUNT
FROM jikwon INNER JOIN buser ON busernum=buserno
WHERE jikwongen='남';

SELECT * FROM gogek; --buser table과는 join 불가(공통 칼럼 X)



--문제
SELECT jikwon.jikwonno AS 사번, jikwon.jikwonname as 직원명, jikwon.jikwonjik AS 직급, gogek.gogekname AS 고객명, gogek.gogektel AS 고객전화,
if(gogek.gogekjumin LIKE '%-1%', '남', '여') as 성별
FROM gogek inner JOin jikwon on jikwonno = gogekdamsano WHERE jikwonjik = '사원';


SELECT jikwon.jikwonno AS 직원, jikwonname as 직원명, COUNT(gogekname) as 고객수
FROM jikwon left outer JOIN gogek on jikwonno = gogekdamsano GROUP BY 직원; 



SELECT jikwon.jikwonname AS 직원명, jikwon.jikwonjik as 직급
FROM jikwon inner JOIN gogek ON jikwonno = gogekdamsano WHERE gogek.gogekname='강나루';


SELECT gogek.gogekname AS 고객명, gogek.gogektel as 고객전화, gogek.gogekjumin as 주민번호, 125 - substring(gogek.gogekjumin,1,2) as 나이
FROM jikwon JOIN gogek ON jikwonno = gogekdamsano WHERE jikwon.jikwonname= '이순신';

	

   
--세개의 테이블 조인 : 두개를 먼저 조인 후 그 결과와 나머지 테이블로 조인...
SELECT jikwonname, busername, gogekname FROM jikwon, buser, gogek
WHERE busernum=buserno AND jikwonno=gogekdamsano;



SELECT jikwonname, busername, gogekname FROM jikwon
INNER join buser on busernum=buserno
inner join gogek on jikwonno=gogekdamsano;











# JOIN 연습2
-- 문제 1 : 총무부에서 관리하는 고객수 출력 (고객 30살 이상만 작업에 참여)
SELECT busername AS 부서, COUNT(*) AS 고객수 
FROM jikwon
INNER JOIN buser ON busernum = buserno
INNER JOIN gogek ON jikwonno = gogekdamsano
WHERE busername = '총무부'  AND (YEAR(SYSDATE()) - (1900 + LEFT(gogekjumin, 2)) + 1) >= 30
GROUP BY busername;

-- 문제 2 : 부서명별 고객 인원수 (부서가 없으면 "무소속")
SELECT nvl(busername,'무소속') AS 부서, COUNT(gogekno) AS 고객수 FROM jikwon
LEFT JOIN buser ON busernum = buserno
LEFT JOIN gogek ON jikwonno = gogekdamsano
GROUP BY busername;

-- 문제 3 : 고객이 담당직원의 자료를 보고 싶을 때 즉, 고객명을 입력하면 담당직원 자료 출력
SELECT jikwonname AS 직원명, jikwonjik AS 직급, busername AS 부서명, 
busertel AS 부서전화, jikwongen AS 성별 FROM jikwon
INNER JOIN buser ON busernum = buserno
INNER JOIN gogek ON jikwonno = gogekdamsano
WHERE gogekname = '강나루';

-- 문제 4 : 부서와 직원명을 입력하면 관리고객 자료 출력
SELECT gogekname AS 고객명, gogektel AS 고객전화,
case
when SUBSTRING(gogekjumin,8,1) IN ('1', '3') then '남'
when SUBSTRING(gogekjumin,8,1) IN ('2', '4') then '여'
ELSE '사람아님'  END AS 성별
FROM jikwon
INNER JOIN buser ON busernum = buserno
INNER JOIN gogek ON jikwonno = gogekdamsano
WHERE busername = '영업부' AND jikwonname = '이순신';




--union : 구조가 일치하는 두개 이상의 테이블 자료 합쳐 출력. 원래 테이블 계속 유지
CREATE TABLE pum1(bun INT, pummok VARCHAR(20));				--int varchar
INSERT INTO pum1 VALUES(1, '귤');
INSERT INTO pum1 VALUES(2,'한라봉');
INSERT INTO pum1 VALUES(3,'바나나');
SELECT * FROM pum1;


CREATE TABLE pum2(nun INT, sangpum VARCHAR(20));				
INSERT INTO pum2 VALUES(10, '토마토');
INSERT INTO pum2 VALUES(20, '딸기');
INSERT INTO pum2 VALUES(30, '참외');
INSERT INTO pum2 VALUES(40, '수박');
SELECT * FROM pum2;


SELECT bun AS 번호, pummok as 품명 from pum1 Union SELECT nun, sangpum from pum2;


--subquery : query 내에 query가 있는 형태(주로 안쪽 질의 결과를 바깥쪽 질의에서 참조)
--다른 테이블의 결과를 조건으로 쓰고 싶을 때
--계산된 값을 이용하고 싶을 때
--복잡한 조건을 단계적으로 나눠 처리하고 싶을 때
--괄호 안이 먼저 수행된다.

--where 안에 있는 subquery
--'이미라' 직원과 직급이 같은 직원 출력
SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라';		--대리
SELECT * FROM jikwon WHERE jikwonjik ='대리';

SELECT * FROM jikwon WHERE jikwonjik =(SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라');

--직급이 대리중에서 가장 먼저 입사한 직원은?
SELECT * FROM jikwon WHERE jikwonibsail = (SELECT MIN(jikwonibsail) FROM jikwon WHERE jikwonjik='대리');


--인천에 근무하는 직원 출려

SELECT FROM jikwon
WHERE busernum = (SELECT buserno FROM buser WHERE buserloc='인천');





--인천 이외에 근무하는 직원 출력
SELECT * FROM jikwon
WHERE busernum IN (SELECT buserno FROM buser WHERE not buserloc='인천');


SELECT * FROM jikwon
WHERE busernum <> (SELECT buserno FROM buser WHERE buserloc='인천');


--고객 중 차일호와 나이가 같은 자료 출력
SELECT * FROM gogek
WHERE SUBSTRING(gogekjumin,1,2)=(SELECT SUBSTRING(gogekjumin,1,2) FROM gogek WHERE gogekname='차일호');


--문제1) 2010년 이후에 입사한 남자 중 급여을 가장 많이 받은 직원은?
SELECT * FROM jikwon
WHERE jikwonibsail >= '2010-1-1' and jikwongen = '남' ANd jikwonpay = (SELECt MAx(jikwonpay) FROm jikwon 
WHERE jikwongen = '남' ANd SUBSTRINg(jikwonibsail, 1, 4) >= 2010);


--문제2) 평균 급여보다 급여를 많이 받는 직원은?
SELECT * FROM jikwon WHERE jikwonpa > (SELECT AVG(jikwonpay) FROM jikwon);


--문제3) '이미라' 직원의 입사 이후에 입사한 직원은?
SELECT * FROM jikwon
WHERE jikwonibsail >= (SELECT jikwonibsail FROM jikwon WHERE jikwonname = '이미라')
ORDER BY jikwonibsail;


--문제4) 2010 ~ 2015년 사이에 입사한 총무부(10), 영업부(20), 전산부(30) 직원중 급여가 가장 적은 사람은?
--(직급이 null인 자료는 작업에서 제외)
SELECT * FROM jikwon
WHERE jikwonibsail BETWEEN '2010-1-1' AND '2015-12-31' AND
jikwonpay = (SELECT MIN(jikwonpay) FROM jikwon
WHERE jikwonibsail BETWEEN '2010-1-1' AND '2015-12-31' AND busernum IN(10, 20, 30))
AND jikwonjik IS NOT NULL;


--문제5) 한송이, 이순신과 직급이 같은 사람은 누구인가?
SELECT * FROM jikwon
WHERE jikwonjik IN (SELECT jikwonjik FROM jikwon
WHERE jikwonname = '한송이' or jikwonname = '이순신') ORder by jikwonjik;


--문제6)  과장 중에서 최대급여, 최소급여를 받는 사람은?
SELECT * FROM jikwon
WHERE jikwonjik = '과장' And jikwonpay IN ((SELECT Max(jikwonpay) FRom jikwon WHEre jikwonjik = '과장'), 
(SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik = '과장'));

-- 문7) 10번 부서의 최소급여보다 많은 사람은?
SELECT * FROM jikwon WHERE jikwonpay > (SELECT MIN(jikwonpay) FROM jikwon WHERE busernum = 10);

-- 문8) 30번 부서의 평균급여보다 급여가 많은 '대리' 는 몇명인가?
SELECT COUNT(jikwonno) FROM jikwon WHERE jikwonjik = '대리' AND jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum = 30);

-- 문9) 고객을 확보하고 있는 직원들의 이름, 직급, 부서명을 입사일 별로 출력하라.
SELECT jikwonname AS 직원명, jikwonjik AS 직급, busername AS 부서명, jikwonibsail AS 입사일  FROM jikwon 
LEFT OUTER JOIN buser ON busernum = buserno WHERE jikwonno IN (SELECT distinct gogekdamsano FROM gogek) ORDER BY jikwonibsail;

-- 문10) 이순신과 같은 부서에 근무하는 직원과 해당 직원이 관리하는 고객 출력(고객은 나이가 30 -> 40 이하면 '청년', 50 이하면 '중년', 그 외는 '노년'으로 표시하고, 고객 연장자 부터 출력)
SELECT jikwonname AS 직원명, busername AS 부서명, busertel AS 부서전화, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화, 
case when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) <= 40 then '청년' when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) <= 50 then '중년' 
when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) > 50 then '노년' ELSE '없음' END AS '고객구분' FROM jikwon
inner JOIN buser ON busernum = buserno inner JOIN gogek ON jikwonno = gogekdamsano 
WHERE busernum = (SELECT busernum FROM jikwon WHERE jikwonname = '이순신')
ORDER BY (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) DESC;




--쿼리문은 동일한 결과를 여러 방법으로 수행 가능
--총무부에 근무하는 직원들이 관리하는 고객 출력
--subquery 사용
SELECT gogekno, gogekname, gogektel FROM gogek
WHERE gogekdamsano IN (SELECT jikwonno FROM jikwon
WHERE busernum = (SELECT buserno FROM buser WHERE busername = '총무부'));

--join 사용
SELECT gogekno, gogekname, gogektel FROM gogek
INNER JOIN jikwon ON jikwon.jikwonno=gogek.gogekdamsano
INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE busername = '총무부';


-- any, all 연산자 : null인 자료는 제외하고 작업한다.
-- <any : subquery의 반환값 중 최대값 보다 작은 ~
-- >any : subquery의 반환값 중 최소값 보다 큰 ~
-- <all : subquery의 반환값 중 최소값 보다 작은 ~
-- >all : subquery의 반환값 중 최대값 보다 큰 ~

--'대리'의 최대값보다 작은 연봉을 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay < any(SELECT jikwonpay FROM jikwon WHERE jikwonjik = '대리');

--30번 부서의 최고 연봉자 보다 연봉을 더 많이 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay > ALL(select jikwonpay FROM jikwon WHERE busernum = 30);


--30번 부서의 최저 연봉자 보다 연봉을 더 많이 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay > ANY (select jikwonpay FROM jikwon WHERE busernum = 30);




--exists 연산자
SELECT DISTINCT busernum FROM jikwon;
--직원이 있는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum = bu.buserno); --true 반환

--직원이 없는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE not EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum = bu.buserno); --false 반환


--from 절에 사용하는 subquery(자주 보기 어려운 형태)
--전체 평균 연봉과 최대 연봉 사이의 연봉을 받는 직원 출력
SELECT jikwonno, jikwonname, jikwonpay 
FROM jikwon a, (SELECT AVG(jikwonpay) avgs, MAX(jikwonpay) maxs FROM jikwon) b
WHERE a.jikwonpay BETWEEN b.avgs AND b.maxs;


--group by의 having 절에 포함된 subquery
--부서별 평균 연봉 중 30번 부서의 평균 연봉보다 큰 자료(부서) 출력
SELECT busernum, AVG(jikwonpay) FROM jikwon 
GROUP BY busernum
HAVING AVG(jikwonpay)>(SELECT AVG(jikwonpay) FROM jikwon WHERE busernum = 30);


--상관 서브쿼리: outer query의 각 행을 inner query에서 참조하여 수행하는 서브 쿼리
--안쪽 질의에서 바깥쪽 질의를 참조하고, 다시 안쪽의 결과를 바깥쪽 질의에서 참조하는 형태(시험 볼 때 좀 나온다.)
--각 부서의 최대 연봉자는?
SELECT * FROM jikwon a
WHERE a.jikwonpay = (SELECT MAX(b.jikwonpay) FROM jikwon b WHERE a.busernum=b.busernum);



--a를 subquery에서 참조한다.
--연봉 순위 3위 이내의 직원 출력(descending 내림 차순 정렬)
SELECT a.jikwonno, a.jikwonname, a.jikwonpay FROM jikwon a
WHERE 3 > (SELECT COUNT(*) FROM jikwon b WHERE b.jikwonpay > a.jikwonpay)
AND jikwonpay IS NOT NULL ORDER BY jikwonpay DESC;


--subquery를 이용한 table 생성 및 insert 수행
CREATE TABLE jiktab1 AS SELECT * FROM jikwon;		--jikwon과 동일 테이블 생성. but pk는 제외
DESC jiktab1;
DESC jikwon;
SELECT * FROM jiktab1;


CREATE TABLE jiktab2 AS SELECT * FROM jikwon WHERE 1=0;	--jikwon과 통일 구조 테이블 생성
SELECT * FROM jiktab2;
DESC jiktab2;
INSERT INTO jiktab2 SELECT * FROM jikwon WHERE jikwonjik = '과장';		--insert + subquery
SELECT * FROM jiktab2;

INSERT INTO jiktab2(jikwonno, jikwonname, busernum) SELECT jikwonno, jikwonname, busernum 
FROM jikwon WHERE jikwonjik = '대리';
SELECT * FROM jiktab2;



--update + subquery
SELECT * from jiktab1;
UPDATE jiktab1 SET jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonname='이순신')
WHERE jikwonno = 2;


--delete + subquery
DELETE FROM jiktab1 WHERE jikwonno IN (SELECT DISTINCT gogekdamsano FROM gogek);
SELECT * FROM jiktab1;




--트랜잭션 : DB의 상태를 변경시키는 논리적인 작업 단위
--트랜잭션의 4가지 특징 : ACID
--insert, update, delete 시 트랜잭션 시작됨
--commit, rollback으로 트랜잭션 종료함
--서버종료, 타임아웃 등이 발생해도 트랜잭션 종료함

SHOW VARIABLES LIKE 'autocommit%'; 		--autocommit 설정 확인
SET autocommit = TRUE						--autocommit 설정
SET autocommit = FALSE						--autocommit 해제


--트랜잭션 연습 1
CREATE TABLE jiktab3 AS SELECT * FROM jikwon;
SELECT * FROM jiktab3;

SET autocommit = FALSE
--여기서부터 트랜잭션 시작
DELETE FROM jiktab3 WHERE jikwonno = 2;
SELECT * FROM jiktab3;

--여기까지 지금 트랜잭션이 안끝남
ROLLBACK 		--트랜잭션 종료(DB 서버와 관련 없이 해당 컴에서만 진행)
SELECT * FROM jiktab3;					--2번이 다시 살아남


--여기서부터 트랜잭션 다시 시작
DELETE FROM jiktab3 WHERE jikwonno = 2;
SELECT * FROM jiktab3;

COMMIT			--트랜잭션 종료(DB 서버에 현재 컴(클라이언트)의 내용을 근거로 원본:DB서버 수정
SELECT * FROM jiktab3; 					--2번이 죽음

SET autocommit = TRUE

--트랜잭션 연습 2 : savepoint(저장점)를 이용하여 부분적인 트랜잭션 처리 가능
SET autocommit = False
SELECT * FROM jiktab3 WHERE jikwonno = 4;
UPDATE jiktab3 SET jikwonpay=7777 WHERE jikwonno = 4;
SELECT * FROM jiktab3 WHERE jikwonno = 4;
savepoint a;
UPDATE jiktab3 SET jikwonpay=8888 WHERE jikwonno=5;
SELECT * FROM jiktab3 WHERE jikwonno=5;
ROLLBACK TO savepoint a;			--부분 작업 취소
SELECT * FROM jiktab3 WHERE jikwonno <= 6;
ROLLBACK;								--전체 작업 취소 : 트랜잭션 종료
SELECT * FROM jiktab3 WHERE jikwonno <= 6;

UPDATE jiktab3 SET jikwonpay=9999 WHERE jikwonno=5;
COMMIT;				--트랜잭션 종료
SET autocommit = TRUE
SHOW VARIABLES LIKE 'autocommit%';

--교착상태(DeadLock) : 두개 이상의 트랜잭션이 서로 상대방이 가진 락(lock)을 기다리면서 영원히 진행하지 못하는 상태
--해결책은 트랜잭션을 수행완료 또는 취소하면 된다.
--일관성 유지가 중요
SET automcommit = FALSE
SELECT * FROM jiktab3 WHERE jikwonno = 2;
UPDATE jiktab3 SET jikwonpay =1234 WHERE jikwonno =7;		--트랜잭션 시작
SELECT * FROM jiktab3 WHERE jikwonno = 7;

--이 상태에서 다른 사람이 delete from jiktab3 where jikwonno = 7
--이렇게 하면 멈춘다. ERROR 1205(HY000) : Lock wait timeout exceeded; try restarting transaction


--해결 방법
COMMIT;

--이렇게 하면 mariaDB prompt에서 락 걸린게 풀린다.
SET autocommit = TRUE




--view 파일------------------
--물리적인 테이블을 근거로 select 문(조건 포함)을 파일로 저장하여, 가상의 테이블로 사용한다.
--물리적인 테이블이 아니므로 메모리 소모가 거의 없다.
--복잡하고 긴 쿼리문을 단순화 가능, 보안 강화, 자료의 독립성 확보
--형식 : create or replace view 뷰파일 명 as select 문
--수정 :	alter view 뷰파일 명
--삭제 : drop view 뷰파일 명
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';
--만약 위의 칼럼들만 쓰거나 보여줄 예정이라면, 물리적으로 새로운 테이블을 만드는 것은 낭비이다.
--다른 직급, 부서를 위한 테이블을 계속 만드는 것 또한 낭비이다. 
--따라서 view 파일을 만드는 것이 효율적이다.
CREATE OR REPLACE VIEW v_a AS				
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

	--create 만 하면 생성돼서 한번 더 실행하면 에러 떨어짐 or replace 해주면 수정 계속 가능



--table을 보면 있다. 근데 테이블은 아니다. 마치 테이블처럼 보인다.
SHOW TABLES;
SELECT * FROM v_a;
DESC v_a;

--실제로는 테이블을 실제로 만드는게 아니라 뷰 파일 만들어서 배포한다. 원본은 안줌
SHOW FULL TABLES IN test WHERE table_type LIKE 'view';					--view file 목록만 확인
SELECT SUM(jikwonpay) AS 연봉합 From v_a;

CREATE VIEW v_b AS SELECT * FROM jikwon 
WHERE jikwonname LIKE '김%' Or jikwonname LIKe '이%' or jikwonname LIke '박%';


SELECT * FROM v_b;
SELECT jikwonno, jikwonname, jikwonpay FROM v_b WHERE jikwonjik = '사원';


ALTER TABLE jikwon RENAME kbs;
SELECT * FROM v_b;						에러 : 물리적인 테이블이 사라졌기 때문이다.

ALTER TABLE kbs RENAME jikwon;
SELECT * FROM v_b;						--다시 테이블 이름을 맞춰줘야 함

CREATE OR replace VIEW v_c AS SELECT * FROM jikwon ORDER BY jikwonpay desc;
SELECT * FROM v_c;

--새 컬럼 추가해서 만들기
CREATE VIEW v_d AS SELECT jikwonno, jikwonname, jikwonpay *10000 AS ypay FROM jikwon;
SELECT * FROM v_d;

CREATE VIEW v_e AS SELECT jikwonname, ypay FROM v_d WHERE ypay >= 5000000;
SELECT * FROM v_e;


UPDATE v_e SET jikwonname = '김치국' WHere jikwonname = '김부만'; 
SELECT * FROM v_e;
SELECT * FROM v_d;				--v_d를 확인해봐도 김부만이 김치국으로 바뀌어져 있다. view 파일을 수정하면 원본 테이블이 수정된다.

DELETE FROM v_d WHERE jikwonname = '최미숙';
SELECT * FROM v_d;
SELECT * FROM jikwon;			--원본 테이블에서도 최미숙이 없다. 
DELETE FROM v_d WHERE ypay = 41000000;			--계산에 의해 생성된 칼럼도 조건에 참여할 수 있다
SELECT * FROM v_d;



--UPDATE v_d SET ypay = 1111 WHERE jikwonname = '홍길동'; 		err 원본 테이블에 ypay가 없기 때문에, 계산 결과에 의한 칼럼은 수정 불가능하다.

CREATE OR REPLACE view v_e AS 
SELECT jikwonno, jikwonname, busernum, jikwonpay FROM jikwon; 

SELECT * FROM v_e;
INSERT INTO v_e VALUES(31, '김밥', 20, 5000);			--view의 insert 는 원본 테이블의 not null에 주의, jikwonno와 jikwonname 은 빠지면 안됨
SELECT * FROM v_e;
SELECT * FROM jikwon;

DESC jikwon;

CREATE OR REPLACE VIEW v_f AS
SELECT jikwonno, jikwonname, busernum, jikwonpay, jikwonibsail FROM jikwon
WHERE jikwonibsail<'2015=1=1';


SELECT * FROM v_f;
INSERT info v_f VALUES(32, '공기밥', 10, 6000, '2014-5-6')
INSERT info v_f VALUES(33, '주먹밥', 10, 6000, '2014-5-6')
SELECT * FROM v_f;					--주먹밥이 안보이는 이유는 조건에서 나가서
SELECT * FROM jikwon;


CREATE VIEW v_group AS
SELECT jikwonjik, SUM(jikwonpay) AS hap, AVG (jikwonpay) AS AVG
FROM jikwon GROUP BY jikwonjik;

SELECT * FROM v_group;				--group by 에 의한 view는 참조만 가능하다(insert, update, delete 불가)

CREATE OR REPLACE VIEW v_join AS
SELECT jikwonno, jikwonname, busername, jikwonjik FROM jikwon
INNER JOIN buser ON jikwon.busernum = buser.buserno
WHERE jikwon.busernum IN(10, 20);

SELECT * FROM v_join;

UPDATE v_join SET jikwonname = '손오공' WHere jikwonname='박명화';
SELECT * FROM v_join;

--UPDATE v_join SET jikwonname = '사오정' , busername = '영업부' WHere jikwonname='손오공';		
--에러 : join에 의한 view는 한개의 테이블만 수정에 참여해야 한다.

--DELETE FROM v_join WHERE jikwonname='손오공';
--에러 : 삭제 불가




'''
문1) 사번   이름    부서  직급  근무년수  고객확보

        1   홍길동  영업부 사원     6           O   or  X

조건 : 직급이 없으면 임시직, 전산부 자료는 제외

위의 결과를 위한 뷰파일 v_exam1을 작성
'''
CREATE OR REPLACE view v_exam1 AS 
SELECT distinct jikwonno AS 사번, jikwonname as 이름, busername as 부서, nvl(jikwonjik, '임시직') AS 직급, 
DATE_FOrmat(now(), '%Y')-date_format(jikwonibsail,'%Y') AS 근무년수, 
CASE nvl(gogekname, 'a') WHEN 'a' THEN 'X' ELSE 'O' ENd as 고객확보
FROM jikwon LEFT OUTER JOIN buser ON busernum = buserno
LEFT OUTER JOIN gogek ON jikwonno = gogekdamsano
WHERE busername <> '전산부' or busername is Null;

SELECT * FROM v_exam1;

'''
문2) 부서명   인원수

       영업부     7

조건 : 직원수가 가장 많은 부서 출력

위의 결과를 위한 뷰파일 v_exam2을 작성
'''
CREATE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수
FROM buser
JOIN jikwon ON buser.buserno = jikwon.busernum
GROUP BY busername
HAVING COUNT(*) = (
    SELECT count(*) FROM jikwon GROUP BY busernum ORDER BY COUNT(*) DESC LIMIT 1);



SELECT * FROM v_exam2;
'''
문3) 가장 많은 직원이 입사한 요일에 입사한 직원 출력

    직원명   요일     부서명   부서전화

    한국인  수요일   전산부   222-2222

위의 결과를 위한 뷰파일 v_exam3을 작성  
'''

CREATE VIEW V_EXAM3 AS
SELECT jikwonname AS 직원명,
       DATE_FORMAT(jikwonibsail, '%W') AS 요일,
       busername AS 부서명,
       busertel AS 부서전화
FROM jikwon
left outer JOIN buser ON jikwon.busernum = buser.buserno
WHERE DATE_FORMAT(jikwonibsail, '%W') = (SELECT DATE_FORMAT(jikwonibsail, '%W') FROM jikwon
GROUP BY DATE_FORMAT(jikwonibsail,'%W') HAVING COUNT(*) = (SELECT COUNT(*) FROM jikwon
GROUP BY DATE_FORMAT(jikwonibsail, '%W') ORDER BY COUNT(*) DESC LIMIT 1))
;

SELECT * FROM V_EXAM3;








SELECT jikwonno AS 직원번호, jikwonname as 직원명, jikwonpay as 연봉 
FROM jikwon
WHERE jikwonpay >= 5000 AND jikwonpay<=7000;


SELECT jikwonno AS 직원번호, jikwonname as 직원명, jikwonpay as 연봉 
FROM jikwon
WHERE jikwonpay between 5000 AND 7000;



SELECT * FROM jikwon
WHERE jikwonpay >= (SELECT AVG(jikwonpay) FROM jikwon); 



SELECT DATE_FORMAT(jikwonibsail,'%Y') as 연도, COUNT(*) AS 인원수, avg(jikwonpay) As 연봉평균
FROM jikwon
WHERE DATE_FORMAT(jikwonibsail,'%Y') BETWEEN 2015 AND 2020
GROUP BY DATE_FORMAT(jikwonibsail,'%Y');


SELECT DATE_FORMAT(jikwonibsail,'%Y') as 연도, COUNT(*) AS 인원수, avg(jikwonpay) As 연봉평균
FROM jikwon
WHERE DATE_FORMAT(jikwonibsail,'%Y') BETWEEN 2015 AND 2020
GROUP BY DATE_FORMAT(jikwonibsail,'%Y');

SELECT * FROM jikwon ORDER BY jikwonibsail;




SELECT jikwonno, jikwonname, busername, jikwonjik
FROM jikwon INNER JOIN buser ON buserno = busernum
WHERE jikwonjik = '과장';


SELECT * FROM jikwon;


SELECT jikwonno AS 직원번호, jikwonname as 직원명, jikwonpay as 연봉 
FROM jikwon
WHERE jikwonpay >= 5000 AND jikwonpay<=7000;



SELECT jikwonno AS 직원번호, jikwonname as 직원명, jikwonpay as 연봉 
FROM jikwon
WHERE jikwonpay between 5000 AND 7000;


SELECT * FROM jikwon
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon); 


SELECT DATE_FORMAT(jikwonibsail,'%Y') as 연도, COUNT(*) AS 인원수, avg(jikwonpay) As 연봉평균
FROM jikwon
WHERE DATE_FORMAT(jikwonibsail,'%Y') BETWEEN 2015 AND 2020
GROUP BY DATE_FORMAT(jikwonibsail,'%Y');

SELECT * FROM jikwon ORDER BY jikwonibsail;

SELECT jikwonname AS 직원명, jikwonpay as 급여, COUNt(gogekname) AS 고객수
FROM jikwon LEFT OUTER JOIN gogek ON jikwonno = gogekdamsano
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon)
GROUP BY jikwonno
;

