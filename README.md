# FAISS를 이용한 시맨틱 서치

`FAISS`와 `ElasticSearch`를 이용한 **시맨틱 서치** 토이 프로젝트입니다.

프로젝트에 사용된 여러 라이브러리들이 **리눅스**에서만 지원되기 때문에, **리눅스** 환경에서의 실행만 테스트되었습니다.

설치를 바르게 진행하셨다면 [_corpus.json_](corpus.json) 파일을 원하는 문장으로 채운 후, 커스텀 **시맨틱 서치** API를 만들어 보실 수 있습니다.

<br/>

## 프로젝트 설치

```
# 프로젝트 클론
git clone https://github.com/Huffon/semantic-search-faiss.git
cd semantic-search-faiss

# 아나콘다 환경 생성
conda create -n semantic-search python=3.6
conda activate semantic-search

# 프로젝트 필수 라이브러리 설치
conda install faiss-gpu pytorch cudatoolkit=10.0 -c pytorch
pip install -r requirements.txt
```

- `ElasticSearch`의 사용을 위해서는 **8 버전** 이상의 **JDK**가 필요합니다.

```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
echo $JAVA_HOME
>>> /usr/lib/jvm/java-11-openjdk-amd64/
```

- `ElasticSearch` 인스턴스가 제대로 실행되지 않는 경우, **JAVA_HOME** _path_ 가 잘 설정되어 있는지 확인하셔야 합니다.

```
# ElasticSearch 다운로드
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.0-linux-aarch64.tar.gz

# 다운로드 파일 압축 해제
tar xvf elasticsearch-7.7.0-linux-aarch64.tar.gz

# ElasticSearch 폴더로 이동
cd elasticsearch

# 한국어 토크나이저 Nori 설치
sudo ./bin/elasticsearch-plugin install analysis-nori
```

<br/>

## 실행 및 인퍼런스

- `ElasticSearch`와의 통신을 위해 **ElasticSearch 클라이언트**를 실행합니다:
	- _cf. `ElasticSearch`는 기본적으로 **9200**번 포트를 사용하기 때문에 포트 충돌이 일어나지 않도록 주의합니다._

```bash
./elasticsearch/bin/elasticsearch/bin/elasticsearch
```

- **Flask API** 서버 실행을 위해 다음 코드를 실행합니다. 첫 실행 시에는 **인덱스 생성**으로 인한 _Latency_ 가 있을 수 있습니다:

```bash
python server.py
```

- **인퍼런스**를 위해 다음 요청을 전송합니다:

```bash
http -v POST localhost:5000/search query="코로나"
```

_cf. **http**는 다음 명령어를 통해 설치 가능합니다: `apt-get install httpie`_

<br/>

## 인퍼런스 결과

![](/img/result_a.png)

- **코로나**를 입력했을 때, `ElasticSearch`와 `FAISS`가 내놓은 헤드라인입니다.

![](/img/result_b.png)

- **확진**을 입력했을 때, `ElasticSearch`와 `FAISS`가 내놓은 헤드라인입니다.

<br/>

## 참조
- [FAISS](https://github.com/facebookresearch/faiss)
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
- [How we used Universal Sentence Encoder and FAISS to make our search 10x smarter](https://blog.onebar.io/building-a-semantic-search-engine-using-open-source-components-e15af5ed7885)
- [Python, Django, Elasticsearch를 사용해서 검색엔진 구축하기](https://blog.nerdfactory.ai/2019/04/29/django-elasticsearch-restframework.html)
- [[ElasticSearch][Python] 데이터넣고 검색하기](http://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221494109911)
