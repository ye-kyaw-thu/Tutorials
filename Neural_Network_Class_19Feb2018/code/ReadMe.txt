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

==========

./caffe-model/ အောက်မှာ caffe နဲ့ သက်ဆိုင်တဲ့ ဖိုင် ၃ဖိုင်ရှိနေရပါမယ်။
ဖိုင်တစ်ဖိုင်က ဆိုင်
