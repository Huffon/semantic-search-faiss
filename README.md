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

<br/>

## 실행 및 인퍼런스

- Flask API 서버 실행을 위해 다음 코드를 실행합니다:

```bash
python wsgi.py
```

- 인퍼런스를 위해 다음 코드를 실행합니다:

```bash
http -v POST localhost:5000/search query="코로나 바이러스"
```

<br/>

## 참조
- [FAISS](https://github.com/facebookresearch/faiss)
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
- [How we used Universal Sentence Encoder and FAISS to make our search 10x smarter](https://blog.onebar.io/building-a-semantic-search-engine-using-open-source-components-e15af5ed7885)
- [Python, Django, Elasticsearch를 사용해서 검색엔진 구축하기](https://blog.nerdfactory.ai/2019/04/29/django-elasticsearch-restframework.html)
