def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j: #aynı indexteki sayıyı 2 kez almamamızı sağlar
                return [i, j]
                print(i,j)
            else: #eğer listede target'a uygun değerler yoksa boş liste döndürür
                return[]

nums = [] #boş liste oluşturduk
x= 1 #x için rastgele bir başlangıç ataması
while x != 0 : #x'e 0 girildiğinde listeye sayı almayı bırakır
    x = int(input("liste için sayı giriniz, liste girişi bittiğinde 0'a basınız ")) 
    if x != 0:
        nums.append(x) #aldığımız x sayılarını nums listemize ekler
print("listeniz oluşturuldu:", nums)
target = int(input("hedef sayıyı giriniz:")) #target belirleme
print(twoSum(nums,target)) #fonksiyon çağırma

