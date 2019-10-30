1. mono-phone 对齐训练：
    https://blog.csdn.net/fandaoerji/article/details/50262969
    https://blog.csdn.net/DuishengChen/article/details/52575926
    http://www.huanglu.club/2017/02/20/kaldi-reading-modify-code.html
    
    
    
    $cmd JOB=1 $dir/log/init.log \
    gmm-init-mono $shared_phones_opt "--train-feats=$feats subset-feats --n=10 ark:- ark:-|" $lang/topo $feat_dim \
    $dir/0.mdl $dir/tree || exit 1;
   用少量的数据快速的得到一个初始化的GMM-HMM模型和决策树， 模型保存$dir/0.mdl        $dir/tree 
   
   
   
   if [ $stage -le -2 ]; then
  echo "$0: Compiling training graphs"
  $cmd JOB=1:$nj $dir/log/compile_graphs.JOB.log \
    compile-train-graphs $dir/tree $dir/0.mdl  $lang/L.fst \
    "ark:sym2int.pl --map-oov $oov_sym -f 2- $lang/words.txt < $sdata/JOB/text|" \
    "ark:|gzip -c >$dir/fsts.JOB.gz" || exit 1;
    
    构造一个训练的网络， 从源码级别分析， 是每个句子构造一个phone leavl级别的fst网络。
    
    构造 monophone的解码图就是先将text中的每个句子， 生成一个fst, (比较简单， 类似于语言模型中的g.fst 但是只有一个句子)
    然后和L.fst compostion 形成训练用的音素级别 fst网络 （类似于LG.fst).
    

