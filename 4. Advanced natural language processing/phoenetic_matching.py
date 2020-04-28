#import the library
import fuzzy
#run the soundex function
soundex = fuzzy.soundex(4)
#generate the phonetic form
soundex('natural')
soundex('natuaral')
soundex('language')
soundex('processing')