while true
do
 python train.py 2 0 || echo "App crashed... restarting..." >&2
 echo "Press Ctrl-C to quit." && sleep 1
done
