# for i in {0..31}; do echo $i; perl ~/Developer_expertise_browser/scripts/Cmtr2Auth.perl $i | ~/lookup/splitSecCh.perl a2cmtrS.$i. 32; done
cd /data/play/DEB
for j in {0..31}; do
    for i in {0..31}; do
        zcat a2cmtrS.$i.$j.gz | lsort 4G -t \; -k1,2 | gzip > cmtr2aFullS.$i.$j.s &
    done
    wait
    echo done $j
done
for j in {0..31}; do str="lsort 10G -u --merge -t\; -k1,2"; for i in {0..31}; do str="$str <(zcat cmtr2aFullS.$i.$j.s)"; done; eval $str | gzip > cmtr2aFullS.$j.s; done &
wait
for j in {0..31}; do zcat cmtr2aFullS.$j.s | ~/lookup/s2sBinSorted.perl cmtr2aFullS.$j.tch; done &