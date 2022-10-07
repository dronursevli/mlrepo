!pip install gradio
#%%
import gradio as gr
#%% gradio örnek 1

#ekrana yazılacak içeriği döndüren metot
def greet_user(name):
	return "Hello " + name + " Welcome to Gradio!😎"

#ınterface ile gradio arayüzü oluşturuluyor
#fn=function arayüze veri sağlayacak fonksiyon
#inputs metoda geçilecek parametreler, text, resim, ses sayı vs olabilir. bizde metot text türünde değer alıyor (arayüzden gelen değer için text kutusu)
#aoutputs arayüzde görüntülenecek içerik, bizde çıktı bir metin olacağı için text (arayüze dönecek değerin için text kutusu konulacak)
#Interface fonksiyonu ile bir nesne oluşturuluyor (app)
app =  gr.Interface(fn = greet_user, inputs="text", outputs="text")
#oluşturulan app nesnesi launch ile çalıştırılıyor. sunucu çalıştıran komut bu
#çıktı ekranındaki 127.0.0.1 ile başlayan URL yi tarayıcıya yapıştırıp açabilirsin
app.launch()

#%% örnek 2

def return_multiple(name, number):
    #burada çıktı isim, girilen sayı ve sayının karesi
    result = "Hi {}! 😎. The Mulitple of {} is {}".format(name, number, round(number**2, 2))
    return result
#birden çok girdi var bu nedenle inputsbir liste. ilk parametre test, ikincisi için bir Slider olacak. çıktı için bir text kutusu
app = gr.Interface(fn = return_multiple, inputs=["text", gr.Slider(0, 50)], outputs="text")
app.launch()

#%%
