#
# val = 13;
# print("odd") if (val & 1 == 1) else print("even");
#
#
#
#
# arr = [1,2,7,6,11,0,0];
# arr1 = sorted(arr);
# print(arr);
# print(arr1);
# arr.sort();
# print(arr);
#
# arr = [[1,2],[3,2],[4,1]];
# val = [[False for x in range(len(arr))] for y in range(len(arr[0]))];
# print(val);
#
# for _,_ in arr:
#     print(_+_);
# print("Comparisons");
# a = '2';
# b = str('2');
# c = str(2);
#
# print(a == b);
# print(a == c);
# print(b == c);
# print(a is b);
# print(a is c);
# print(b is c);
#
# # from urllib.request import urlopen;
# # store = urlopen('https://app.pluralsight.com/course-player?clipId=d655883b-90f4-4e21-b841-fcab009e976b');
# # for line in store:
# #     print(line);
# # store.close()
#
# with open('texts') as f:
#     letters = f.read()
#     words = letters.split(" ");
#     letters_as_list = list(letters)
#     print(letters)
#     print(words)
#     print(letters_as_list)
#
#     print(letters.encode())
#
#
# arr = {"obj1": 10, "obj2": 20, "obj3": 100, "obj4": 15};
# print(type(arr))
# for w in sorted(arr, key=arr.get):
#     print(w, arr[w])
#
#
#
#
a = 100
print("Hello here {}".format(a))