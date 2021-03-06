## 카카오톡 대화 분석기  

카카오톡 대화방에서 어떤 단어가 많이 나왔는지 명사 단위로 추출하여 시각화하는 프로그램입니다.

![wordcloud](https://user-images.githubusercontent.com/51525202/85218071-b128cf80-b3d1-11ea-95e8-67c0411fa811.png)

<br/>

## 프로그램 구동

1. **Java**    

한글 형태소를 분석하는 konlpy 라이브러리는 자바 기반으로 구동되기에 JDK가 필수입니다.
파이썬과 자바의 비트를 일치시켜 환경을 구성합니다.

2. **jpype**   

파이썬에서 자바를 구동하기 위한 라이브러리입니다. 파이썬 버전에 맞추어 설치합니다.

3. **requirements.txt**  

그 외 구동에 필요한 라이브러리입니다. 아래 명령어로 설치합니다.

``` 
pip install -r requirements.txt
```

<br/>

## 파일 준비  

1. **카카오톡 log 파일 준비**     
카카오톡 채팅방에서 대화내보내기 기능을 사용하여 txt 파일을 생성합니다.

2. **폰트 파일(.ttf)**   
한글의 경우 폰트 파일을 반드시 지정해야 word cloud가 생성됩니다.

3. **워드클라우드 마스크**   
word cloud 모양을 만들 이미지 파일을 지정합니다. 필수 사항은 아닙니다.

<br/>

해당 파일들을 준비하고 rsc/config.json 파일에 경로를 세팅합니다.

``` json
{
	"raw_file_path" : "./raw_log/log.txt",
	"img_path" : "./mask_img/pepe.jpg",
	"font_path" : "./font/malgunbd.ttf"
}
```