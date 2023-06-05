<img width="522" alt="ismek_photo" src="https://github.com/team-pikachuuuu/BootcampProjects/assets/97554694/23e5643d-5cce-4959-9d2d-4efa64ff5595">


Kodluyoruz ve İBB iş birliği ile gerçekleştirilen K152. Zemin İstanbul Veri Bilimi Python Bootcamp final projesinde İSMEK verileri incelenmiştir, veri analizleri yapılmıştır ve biri kullanıcı diğeri ise kurs merkezi için olmak üzere 2 farklı makine öğrenmesi modeli geliştirilmiştir. 

## Projede kullanılan Veri Seti 
[Veri Seti Linki](https://data.ibb.gov.tr/dataset/2019-2020-yillari-arasindaki-ismek-egitim-alan-vatandas-verisi/resource/acc4c5d6-7654-48fb-a460-bffc6050f1b2)

**Veri setinde bulunan özelliklerin(features) kısa açıklamaları:** 

* **Dönem:** 2019-2020 <br/>
* **Kurs Merkezi İlçesi:** 37 ilçe <br/>
* **Kurs Merkezi:** 190 kurs merkezi <br/>
* **Alan:** 33 alan <br/>
* **Program:** 541 kurs program <br/>
* **Çalışma Durumu:** çalışan, öğrenci, çalışmayan, emekli <br/>
* **Hak Edilen Belge Tipi:** İsmek Sertifika, MEB Sertifika, hak kazanamadı <br/>
* **Engel Durumu:** engelli olmayanlar & engel türleri <br/>
* **Eğitim Durumu:** Lisans, lise, ön lisans vb. <br/>
* **Tercih Sebebi:** hangi amaçla tercih edildiği (4 farklı sınıflandırma) <br/>
* **Yaş Aralığı:** 6 farklı sınıflandırma <br/>



## Amaç
İlk olarak İSMEK kurslarına kaydolmak isteyen **kursiyerler için kurs tercih etme** sürecine yardımcı olabilecek bir kurs tavsiye sistemi tasarlanmıştır -> Alan Modeli <br/>
----------------- <br/>
İkinci modelde ise kurumun kişileri **kursa kabul etme sürecini** kolaylaştıracak bir model tasarlanmıştır -> Haketme Modeli

## Model
Model olarak en iyi sonuçları aldığımız **XGBClassifier** modeli kullanılmıştır.
Modeller geliştirilirken overfit e sebep olan veriler tespit edilerek veriden çıkartılmıştır ve **optuna** ile hiperparametre optimizasyonu yapılmıştır.

## Sonuç
Kişinin bazı kriterlere göre İSMEK kurs önerisi alabileceği model geliştirilerek bir arayüz ile kullanıcıya sunulmuştur. Bu arayüze linkten ulaşabilir ve inceleyebilirsiniz.
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://team-pikachu.streamlit.app/Modeller)

*Not: bu iki model, farklı arayüzlerle sunulmak üzere tasarlanmıştır fakat proje sunum sürecinde daha iyi anlaşılması açısında aynı arayüzde sunulmuştur.*
