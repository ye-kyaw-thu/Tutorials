Bash shell and Python scripts for practical work of Myanmar fingerspelling classification (Ka to Nga Consonants).

အောက်ပါ ပရိုဂရမ်တွေကို သုံးပြီး image classification ကို လက်တွေ့ လုပ်ကြည့်ကြရအောင်
extract-feature.sh (for feature extraction)
add-label.sh (for adding y labels, combining all features as one file for training)
train-test-MLP-clf.py (for training image classifier and testing)

==========

အရင်ဆုံး ./data/ ဖိုလ်ဒါကို mkdir data ဆိုတဲ့ command ပေးပြီး ဖိုလ်ဒါ အသစ်ဆောက်ပါ။
အဲဒီအောက်မှာ ကိုယ်က classification လုပ်ချင်တဲ့ image ဖိုင်တွေကို သက်ဆိုင်ရာ class အလိုက် sub-folder တွေခွဲပြီး သိမ်းပါ။

ဥပမာ class က "ကကြီး" ကနေ "င" အထိ ၅မျိုးရှိတယ်ဆိုရင်၊ အောက်ပါအတိုင်း ဖိုလ်ဒါ ၅ခုရှိရမယ်။

lar@lar-air:~/experiment/fs/mc-fs/ucsy-fs/data$ ls
Ga  Gha  Ka  Kha  Nga 

Ka/ အောက်မှာ ကကြီး ပုံတွေ
Kha/ အောက်မှာ ခကွေး ပုံတွေ
Ga/ အောက်မှာ ဂငယ် ပုံတွေ
Gha/ အောက်မှာ ဃ ပုံတွေ
Nga/ အောက်မှာ င ပုံတွေ ကို အသီးသီး သိမ်းထားပါ။

UCSY ရဲ့ Neural Network class မှာက မိုဘိုင်းဖုန်း ၂လုံးကို သုံးပြီး ပုံ ၁၈၀ ကို ရိုက်ယူခဲ့ပါတယ်။
အဲဒီပုံတွေကိုတော့ တင်မပေးထားပါဘူး။

ကိုယ် ကြိုက်တဲ့ ပုံနဲ့ စမ်းလို့ ရပါတယ်။
class အရေအတွက်ကလည်း ကိုယ်ကြိုက်သလို ထားလို့ ရပါတယ်။

==========

./caffe-model/ အောက်မှာ caffe နဲ့ သက်ဆိုင်တဲ့ ဖိုင် ၃ဖိုင်ရှိနေရပါမယ်။
bvlc_reference_caffenet.caffemodel ဖိုင်က ဖိုင်ဆိုက်ကြီးလို့ GitHub မှာ မတင်ထားပါဘူး။
အောက်ပါ လင့် ကနေ ဒေါင်းလုဒ်လုပ်ယူပါ။
https://github.com/BVLC/caffe/tree/master/models/bvlc_reference_caffenet

==========

./data နဲ့ ./caffe-model ဖိုလ်ဒါပြင်ဆင်တာပြီးပြီ ဆိုရင်run ကြည့်လို့ ရပြီ။

==========

Running Steps:

Feature extraction လုပ်တဲ့ အဆင့်:
$time ./extract-feature.sh ./data/ | tee train-test.log

train လုပ်လို့ရအောင် တစ်ပုံချင်းစီရဲ့ feature တွေကို ဖိုင်တစ်ဖိုင်ထဲမှာ လေဘယ် (နောက်ဆုံး ကော်လံမှာရှိ) တပ်ပြီး သိမ်းတဲ့ အလုပ်ကို လုပ်ဖို့၊
နောက်ပြီးတော့ id နဲ့ class name dictionary ဆောက်တဲ့ အလုပ်ကို လုပ်ဖို့အတွက်က အောက်ပါ command ကို run ပါ။
$./add-label.sh ./data/ | tee ./train-test.log 

Multilayer perceptron (MLP) နဲ့ classifier modeling (i.e. training) နဲ့ testing ကို လုပ်ဖို့အတွက်က အောက်ပါ command ကို run ပါ။ 
$python ./train-test-MLP-clf.py ./data/data.feature | tee ./train-test.log 

