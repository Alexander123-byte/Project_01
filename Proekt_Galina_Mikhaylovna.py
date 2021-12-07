from tkinter import *
from tkinter import messagebox

#окно приложения
win = Tk()
win.geometry("250x350")
win.title("Часовые зоны в регионах страны")

#текст выбора региона
var1 = IntVar()
var1.set(0)

def Click():
    if var1.get() == 0:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 - 1
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 10 <= minut < 60 and 1 <= Chas < 10:
            message="Время в Калининградском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 1 <= Chas < 10:
            message="Время в Калининнрадском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == -1:
            message = "Время в Калининградском регионе: 23:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == -1:
            message = "Время в Калининградском регионе: 23:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 0:
            message = "Время в Калининградском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 0:
            message = "Время в Калининградском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 1 < minut < 10 and 1 <= Chas < 10 :
            message = "Время в Калининградском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 < Chas < 24:
            message = "Время в Калининградском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Калининградском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message) 
        
    elif var1.get() == 1:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Московском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10 :
            message = "Время в Московском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 < Chas < 24:
            message = "Время в Московском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Московском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 2:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 1
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Самарском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and 1 <= Chas < 10:
            message="Время в Самарском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Самарском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Самарском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время в Самарском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 <= Chas < 24:
            message = "Время в Самарском регионе: " + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Самарском регионе: " + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 3:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 2
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Екатеринбургском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Екатеринбургском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Екатеринбургском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Екатеринбургском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Екатеринбургском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время в Екатеринбургском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 <= Chas < 24:
            message = "Время в Екатеринбургском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Екатеринбургском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 4:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 3
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if Chas == 0 and 0 <= minut < 60:
            message="Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif Chas == 1 and 0 <= minut < 60:
            message="Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif Chas == 2 and 0 <= minut < 60:
            message="Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Омском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время в Омском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Омском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Омском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Омском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Омском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Омском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Омском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время в Омском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 <= Chas < 24:
            message = "Время в Омском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Омском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message) 
            
    elif var1.get() == 5:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 4
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Красноярском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время в Красноярском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Красноярском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Красноярском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Красноярском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Красноярском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Красноярском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Красноярском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время в Красноярском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время в Красноярском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время в Красноярском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and 10 <= Chas < 24:
            message = "Время в Красноярском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Красноярском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 6:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 5
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 4:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Иркутском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время в Иркутском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Иркутском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Иркутском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Иркутском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Иркутском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Иркутском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Иркутском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время в Иркутском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время в Иркутском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 28:
            message = "Время в Иркутском регионе: 04:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 28:
            message = "Время в Иркутском регионе: 04:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10:
            message = "Время в Иркутском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 10 <= Chas < 24:
            message = "Время в Иркутском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Иркутском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 7:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 6
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 4:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 5:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Якутском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время в Якутском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Якутском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Якутском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Якутском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Якутском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Якутском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Якутском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время в Якутском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время в Якутском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 28:
            message = "Время в Якутском регионе: 04:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 28:
            message = "Время в Якутском регионе: 04:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 29:
            message = "Время в Якутском регионе: 05:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 29:
            message = "Время в Якутском регионе: 05:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время в Якутском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 10 <= Chas < 24:
            message = "Время в Якутском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Якутском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 8:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 7
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 4:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 5:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 6:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время во Владивостокском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время во Владивостокском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время во Владивостокском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время во Владивостокском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время во Владивостокском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время во Владивостокском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время во Владивостокском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время во Владивостокском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время во Владивостокском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время во Владивостокском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 28:
            message = "Время во Владивостокском регионе: 04:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 28:
            message = "Время во Владивостокском регионе: 04:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 29:
            message = "Время во Владивостокском регионе: 05:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 29:
            message = "Время во Владивостокском регионе: 05:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 30:
            message = "Время во Владивостокском регионе: 06:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 30:
            message = "Время во Владивостокском регионе: 06:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message = "Время во Владивостокском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 10 <= Chas < 24:
            message = "Время во Владивостокском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время во Владивостокском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 9:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 8
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 4:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 5:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 6:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 7:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message="Время в Среднеколымском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message="Время в Среднеколымском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Среднеколымском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Среднеколымском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Среднеколымском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Среднеколымском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Среднеколымском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Среднеколымском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время в Среднеколымском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время в Среднеколымском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 28:
            message = "Время в Среднеколымском регионе: 04:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 28:
            message = "Время в Среднеколымском регионе: 04:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 29:
            message = "Время в Среднеколымском регионе: 05:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 29:
            message = "Время в Среднеколымском регионе: 05:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 30:
            message = "Время в Среднеколымском регионе: 06:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 30:
            message = "Время в Среднеколымском регионе: 06:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 31:
            message = "Время в Среднеколымском регионе: 07:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 31:
            message = "Время в Среднеколымском регионе: 07:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10:
            message = "Время в Среднеколымском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 10 <= Chas < 24:
            message = "Время в Среднеколымском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Среднеколымском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)

    elif var1.get() == 10:
        Chas = 0
        minut = 0
        time_1 = chas.get()
        time_new = time_1 + 9
        time_2 = min.get()
        minut += time_2
        Chas += time_new
        if 0 <= minut < 60 and Chas == 0:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 1:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 2:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 3:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 4:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 5:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 6:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 7:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 0 <= minut < 60 and Chas == 8:
            message = "Проверьте правильность введенных данных"
            messagebox.showwarning("Ошибка", message)
        elif 10 <= minut < 60 and 0 <= Chas < 10:
            message = "Время в Камчатском регионе: 0" + str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 0 <= Chas < 10:
            message = "Время в Камчатском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 24:
            message = "Время в Камчатском регионе: 00:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 24:
            message = "Время в Камчатском регионе: 00:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 25:
            message = "Время в Камчатском регионе: 01:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 25:
            message = "Время в Камчатском регионе: 01:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 26:
            message = "Время в Камчатском регионе: 02:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 26:
            message = "Время в Камчатском регионе: 02:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 27:
            message = "Время в Камчатском регионе: 03:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 27:
            message = "Время в Камчатском регионе: 03:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 28:
            message = "Время в Камчатском регионе: 04:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 28:
            message = "Время в Камчатском регионе: 04:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 29:
            message = "Время в Камчатском регионе: 05:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 29:
            message = "Время в Камчатском регионе: 05:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 30:
            message = "Время в Камчатском регионе: 06:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 30:
            message = "Время в Камчатском регионе: 06:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 31:
            message = "Время в Камчатском регионе: 07:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 31:
            message = "Время в Камчатском регионе: 07:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif minut < 10 and Chas == 32:
            message = "Время в Камчатском регионе: 08:" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= minut < 60 and Chas == 32:
            message = "Время в Камчатском регионе: 08:" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 1 <= Chas < 10 :
            message  = "Время в Камчатском регионе: 0" + str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 0 <= minut < 10 and 10 <= Chas < 24:
            message = "Время в Камчатском регионе: "+ str(Chas) + ":" + "0" + str(minut)
            messagebox.showinfo("Результат", message)
        elif 10 <= Chas < 24 and 10 <= minut < 60:
            message = "Время в Камчатском регионе: "+ str(Chas) + ":" + str(minut)
            messagebox.showinfo("Результат", message)
            
    with open('Change_Log.txt', 'a') as file:
        file.write(message+'\n')


vibor_rg = Label(text = "Выберите регион:",
                      font = 20
                      )
vibor_rg.place(x = 7, y = 50)

#кнопки выбора региона
Kalin = Radiobutton(text = "Калининградский регион",
                    padx = 15, pady = 0,
                    value = 0, variable = var1
                    )
Kalin.place(x = 1, y = 80)

Moscow = Radiobutton(text = "Московский регион",
                    padx = 15, pady = 0,
                    value = 1, variable = var1
                    )
Moscow.place(x = 1, y = 100)

Samara = Radiobutton(text = "Самарский регион",
                    padx = 15, pady = 0,
                    value = 2, variable = var1
                    )
Samara.place(x = 1, y = 120)

Ekater = Radiobutton(text = "Екатеринбургский регион",
                    padx = 15, pady = 0,
                    value = 3, variable = var1
                    )
Ekater.place(x = 1, y = 140)

Omsk = Radiobutton(text = "Омский регион",
                    padx = 15, pady = 0,
                    value = 4, variable = var1
                    )
Omsk.place(x = 1, y = 160)

Krasn = Radiobutton(text = "Красноярский регион",
                    padx = 15, pady = 0,
                    value = 5, variable = var1
                    )
Krasn.place(x = 1, y = 180)

Irkutsk = Radiobutton(text = "Иркутский регион",
                    padx = 15, pady = 0,
                    value = 6, variable = var1
                    )
Irkutsk.place(x = 1, y = 200)

Yakutsk = Radiobutton(text = "Якутский регион",
                    padx = 15, pady = 0,
                    value = 7, variable = var1
                    )
Yakutsk.place(x = 1, y = 220)

Vladik = Radiobutton(text = "Владивостокский регион",
                    padx = 15, pady = 0,
                    value = 8, variable = var1
                    )
Vladik.place(x = 1, y = 240)

Sr_Kol = Radiobutton(text = "Среднеколымский регион",
                    padx = 15, pady = 0,
                    value = 9, variable = var1
                    )
Sr_Kol.place(x = 1, y = 260)

Kam4 = Radiobutton(text = "Камчатский регион",
                    padx = 15, pady = 0,
                    value = 10, variable = var1
                    )
Kam4.place(x = 1, y = 280)

#Кнопка
knopka = Button(text = "Узнать время", command = Click)
knopka.place(x = 70, y = 310)

#Подпись "часы"
pod_chas = "Введите часы:"
label1 = Label(text = pod_chas)
label1.place(x = 7, y = 1)

#Поле ввода часов
chas = IntVar()
chas_pole = Entry(textvariable = chas, width = 15)
chas_pole.place(x = 10, y = 25)

#Подпись "минуты"
pod_min = "Введите минуты:"
label2 = Label(text = pod_min)
label2.place(x = 127, y = 1)

#Поле ввода минут
min = IntVar()
min_pole = Entry(textvariable = min, width = 15)
min_pole.place(x = 130, y = 25)

dvoe_toch = ":"
label3 = Label(text = dvoe_toch)
label3.place(x = 113, y = 25)

win.mainloop()