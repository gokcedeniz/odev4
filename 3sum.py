def threeSum (nums):
        nums.sort()
        n, result = len(nums), []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            j =i+1
            k =n-1
            while j<k:
                if nums[j]+nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j+1
                    while j<k and nums[j] == nums[j-1]:
                        j = j+1
                elif nums[j] + nums[k] < target:
                    j = j+1
                else:
                    k = k-1
        return result

nums = [] 
x= 1 #x için rastgele bir başlangıç ataması
while x != 0 : 
    x = int(input("liste için sayı giriniz, liste girişi bittiğinde 0'a basınız ")) 
    if x != 0:
        nums.append(x) 
print("listeniz oluşturuldu:", nums)
print(threeSum(nums)) 
