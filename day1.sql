CREATE TABLE dept(NO INT PRIMARY KEY, NAME VARCHAR(10), tel VARCHAR(15), inwon INT, addr TEXT) CHARSET = UTF8; --테이블 생성

--자료 추가
#insert into 테이블명(칼럼명,....NO) values(입력자료,....)
INSERT INTO dept(NO ,NAME, tel, inwon, addr) VALUES(1, '인사과', '111-1111', 3, '삼성동12');
INSERT INTO dept VALUES(2, '영업과', '111-2222', 5, '서초동12');
INSERT INTO dept (NO ,NAME) VALUES(3, '자재과');
INSERT INTO dept (NO, addr, tel, NAME) VALUES(4,'역삼2동33', '111-5555',  '자재2과');


--에러
#INSERT INTO dept VALUES(5, '판매과');																					--err : 입력 자료와 칼럼 갯수 불일치
#INSERT INTO dept (NAME ,tel) VALUES('판매과2', '111-6666');														--err : NO:pk, 생략 불가
#INSERT INTO dept (NO, NAME) VALUES(5, '판매과부서는 사람들이 좋아 일하기 좋은 우수한 부서임');		--err : NAME 칼럼을 10자리로 생성했는데 넘어갔음 overflow

SELECT * FROM dept;

SELECT * FROM dept WHERE NO =1;



--자료 수정
--update 테이블명 set 수정칼럼명=수정값, .... where 조건 <= 수정 대상 칼럼을 지정
--pk 칼럼의 자료는 수정 대상에서 제외
UPDATE dept SET tel='123-4567' WHERE NO=2;
--where no=2를 쓰지 않으면 전화번호 전부다 바뀜. 돌이킬 수 없다고 생각해라
UPDATE dept SET addr='압구정동33', inwon=7, tel='777-8888' WHERE NO=3;

SELECT * FROM dept;


--자료 삭제
--delete from 테이블명 where 조건		--전체 또는 부분적 레코드 삭제 가능
--truncate table 테이블명 					--where 조건을 사용 X, 전체 레코드 삭제 가능 칼럼명만 남음
DELETE FROM dept WHERE name='자재2과';
truncate TABLE dept;
SELECT * FROM dept;


DROP TABLE dept; --테이블 자체(구조, 자료)가 제거

--무결성 제약조건: 테이블 생성 시 잘못된 자료 입력을 막고자 다양한 입력 제한 조건을 줄 수 있다.
--1) 기본키 제약: primary key(pk) 사용, 중복 레코드 입력 방지
CREATE TABLE aa(bun INT PRIMARY KEY, irum CHAR(10));				--bun: NOT NULL, UNIQUE 이 컬럼이 없으면 입력이 안되며, 중복이 불가능하다.
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE table_name='aa';
INSERT INTO aa VALUES(1,'tom');
INSERT INTO aa VALUES(2,'tom');											--이름은 중복 가능하다.
--INSERT INTO aa(irum) VALUES('tom');									pk 에러
INSERT INTO aa(bun) VALUES('3');
SELECT * FROM aa;
DROP TABLE aa;



CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_bun_pk PRIMARY KEY(bun));
INSERT INTO aa VALUES(1,'tom');
SELECT * FROM aa;
DROP TABLE aa;

--2) check 제약: 입력 자료의 특정 칼럼값 조건 검사
CREATE TABLE aa(bun INT, nai INT, CHECK(nai >= 20));
INSERT INTO aa VALUES(1,23);
--INSERT INTO aa VALUES(2,13);				--에러: 조건에 맞지 않음
SELECT * FROM aa;
DROP TABLE aa;


--3) unique 제약: 특정 칼럼값 중복 불허
CREATE TABLE aa(bun INT, irum CHAR(10) NOT NULL UNIQUE);
INSERT INTO aa VALUES(1, 'tom');
INSERT INTO aa VALUES(2, 'john');
--INSERT INTO aa VALUES(3, 'john');			--에러 : 중복 불가
SELECT * FROM aa;
DROP TABLE aa;


--4) foreing key(fk), 외부키, 참조키 제약, 특정 칼럼이 다른 테이블의 칼럼을 참조
--fk 대상은 pk다!!!
CREATE TABLE jikwon(bun INT PRIMARY KEY, irum VARCHAR(10) NOT NULL, buser CHAR(10) NOT NULL);
INSERT INTO jikwon VALUES(1, '한송이', '인사과');
INSERT INTO jikwon VALUES(2, '이기자', '인사과');
INSERT INTO jikwon VALUES(3, '한국인', '판매과');
SELECT * from jikwon;


CREATE TABLE gajok(code INT PRIMARY KEY, name VARCHAR(10) NOT NULL, birth DATETIME, jikwonbun INT, FOREIGN KEY(jikwonbun) references jikwon(jikwonno));   --칼럼명은 달라도 되지만 자료형은 같아야 한다(pk와)

INSERT INTO gajok VALUES(10,'한가해', '2015-05-12',3);
INSERT INTO gajok VALUES(20,'공기밥', '2011-12-12',2);
--INSERT INTO gajok VALUES(30,'김밥', '2013-12-12',5); 		에러 : 5번이 없다.
INSERT INTO gajok VALUES(30,'심심해', '2010-05-12',3);
SELECT * FROM gajok;

DELETE FROM jikwon WHERE bun=1;
SELECT * FROM jikwon;
--DELETE FROM jikwon WHERE bun=3;									에러 : 참조 자료(가족)가 있으므로 삭제 불가
--DROP TABLE jikwon;														에러 : 마찬가지로 삭제 불가
SELECT * FROM jikwon;

DELETE FROM gajok WHERE jikwonbun=2;								--참조키(pk)가 2번인 가족자료 삭제
DELETE FROM jikwon WHERE bun=2;										--참조 가족이 없으므로 2번 직원 삭제 가능
SELECT * FROM jikwon; 

--참고
--create table gajok(code int primary key, ...) on delete cascade
--직원 자료를 삭제하면 관련 있는 가족 자료도 함께 지워진다.
--위험한 명령 실무에선 웬만하면 안씀 -> 파이썬에서 코드를 짠다 보통

DROP TABLE gajok;
DROP TABLE jikwon;


--default : 특정 칼럼에 초기치 부여.null 예방
CREATE TABLE aa(bun INT PRIMARY KEY AUTO_INCREMENT, juso CHAR(20) DEFAULT'강남구 역삼동'); --AUTO_INCREMENT : bun 자동 증가
INSERT INTO aa VALUES(1, '서초구 서초2동');
INSERT INTO aa(juso) VALUES('서초구 서초3동');
INSERT INTO aa(juso) VALUES('서초구 서초4동');
INSERT INTO aa(bun) VALUES(5);
INSERT INTO aa(bun) VALUES(6);								--주소를 안적으면 default가 들어가게 된다.
SELECT * FROM aa;

DROP TABLE aa;




CREATE TABLE gyosu(
	gyoco INT PRIMARY KEY, 
   gyomyung VARCHAR(10), 
   gyonum INT, 
   CHECK(gyonum>=100), 
   CHECK(gyonum<=500)
   );

CREATE TABLE gwamok(
	gwaco INT PRIMARY KEY AUTO_INCREMENT, 
   gwamyung VARCHAR(10) NOT NULL UNIQUE, 
   gyoname VARCHAR(10), 
   damgyo INT, 
   FOREIGN KEY(damgyo) REFERENCES gyosu(gyoco)
   );

CREATE TABLE hak(
	hakbun INT PRIMARY KEY, 
   hakmyung VARCHAR(10), 
   sumok INT NOT NULL, 
   haknum INT DEFAULT 1,
   CHECK(haknum <= 4 AND haknum >= 1),
   FOREIGN KEY(sumok) REFERENCES gwamok(gwaco)
   );


DROP TABLE hak, gwamok, gyosu;


INSERT INTO gyosu VALUES(1, '이인수', 101);
INSERT INTO gyosu VALUES(2, '박유성', 401); 

SELECT * FROM gyosu;

INSERT INTO gwamok VALUES(32, '수학', '이인수', 1);

SELECT * FROM gwamok;



--primary key를 주게되면 자동으로 인덱스가 생기며, select를 하게 되면 오름차순으로 정렬되어있는 것을 확인할 수 있다.
--검색 속도를 빨리 하기 위해서 자주 쓰이는 칼럼에 대해서 index를 만들어준다.
--단점: 메모리를 많이 잡아먹는다. 자료를 자주 수정하다 보면 인덱스를 재구성해야 한다.


--index(색인) : 검색 속도 향상을 위해 특정 column에 색인 부여 가능
--pk column은 자동으로 인덱싱됨(ascending sort 오름차순 정렬)
--index를 자제해야 하는 경우: 입력, 수정, 삭제, 등의 작업이 빈번한 경우
CREATE TABLE aa(
	bun INT PRIMARY KEY, 
   irum VARCHAR(10) NOT NULL,
   juso VARCHAR(50)
   );
   
INSERT INTO aa VALUES(1, '신선해', '테헤란로111');
ALTER TABLE aa ADD INDEX ind_juso(juso);					--juso column에 index 부여
ALTER TABLE aa DROP INDEX ind_juso;
SELECT * FROM aa;



EXPLAIN SELECT * FROM aa;
DESC aa;
SHOW INDEX FROM aa;			--A는 어센딩, D는 디센딩 인덱스 타입이 BTREE이다. Hash가 올 수도 있다. 
--BTREE는 이진 검색이다. 1번부터 10번까지 있으면 반 짤라서 위에 있는지 아래 있는지 보는 것(이진트리)

DROP TABLE aa;

--테이블 관련 주요 명령
--CREATE TABLE 테이블명 ...
--ALTER TABLE 테이블명 ...
--DROP TABLE 테이블명...
CREATE TABLE aa(
	bun INT, 
   irum VARCHAR(10),
   juso VARCHAR(50)
   );

INSERT INTO aa VALUES(1, 'tom', 'seoul');
SELECT * FROM aa;

ALTER TABLE aa RENAME kbs;
SELECT * FROM kbs;

ALTER TABLE kbs RENAME aa;

--칼럼 관련 명령
ALTER TABLE aa ADD(job_id INT DEFAULT 10); 		--칼럼 추가
SELECT * FROM aa;

ALTER TABLE aa CHANGE job_id job_num INT; 		--칼럼 수정(이름이나 성격 변경 가능)
SELECT * FROM aa;

ALTER TABLE aa MODIFY job_num VARCHAR(10);		--칼럼 성격 변경
DESC aa;

ALTER TABLE aa DROP COLUMN job_num;					--칼럼 삭제
DESC aa;




create table emp (eno INT PRIMARY KEY, ename varchar(10), job varchar(9), pay INT, CHECK(pay>=2000) );
INSERT INTO emp values(1, 'dldl', 'df', 200);



DELETE FROM buser WHERE buserno = 3;
SELECT * FROM buser;
INSERT INTO buser VALUES(3, '바바바', '경기', 123123);



CREATE TABLE customers(cno INT PRIMARY KEY, cname CHAR(10), caddress VARCHAR(50), cemail CHAR(20), cphone VARCHAR(20));

CREATE TABLE orders(ono INT PRIMARY KEY, odate DATETIME, oaddress VARCHAR(50), ophone VARCHAR(20), ostatus VARCHAR(10), 
ono_cus INT, FOREIGN KEY(ono_cus) REFERENCES customers(cno));

DESC customers;
DESC orders;
DESC gajok;
