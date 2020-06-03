# FAISS를 이용한 시맨틱 서치

FAISS와 ElasticSearch를 이용한 시맨틱 서치 토이 프로젝트

<br/>

## 설치

```
git clone https://github.com/Huffon/semantic-search-faiss.git
cd semantic-search-faiss

conda create -n semantic-search python=3.6
conda activate semantic-search

conda install faiss-gpu pytorch cudatoolkit=10.0 -c pytorch
pip install -r requirements.txt
```

- ElasticSearch 사용을 위해서는 8 버전 이상의 JDK가 필요합니다.

```
# ElasticSearch 다운로드
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.0-linux-aarch64.tar.gz

# 다운로드 파일 압축 해제
tar xvf elasticsearch-7.7.0-linux-aarch64.tar.gz

# ElasticSearch 폴더로 이동
cd elasticsearch

# 한국어 토크나이저 Nori 설치
sudo ./bin/elasticsearch-plugin install analysis-nori

# ElasticSearch 실행
./bin/elasticsearch/bin/elasticsearch
```

<br/>

## 실행 및 인퍼런스

- Flask API 서버 실행을 위해 다음 코드를 실행합니다:

```bash
gunicorn server:app --bind=0.0.0.0:8018 -w 4
```

- 인퍼런스를 위해 다음 코드를 실행합니다:

```bash
http -v POST localhost:8018/search query="코로나 바이러스"
```

<br/>

## 참조
- [FAISS](https://github.com/facebookresearch/faiss)
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
- [How we used Universal Sentence Encoder and FAISS to make our search 10x smarter](https://blog.onebar.io/building-a-semantic-search-engine-using-open-source-components-e15af5ed7885)
- [Python, Django, Elasticsearch를 사용해서 검색엔진 구축하기](https://blog.nerdfactory.ai/2019/04/29/django-elasticsearch-restframework.html)
