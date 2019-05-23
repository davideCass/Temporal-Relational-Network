# Temporal-Relational-Network
Progetto di Machine Learning e Sistemi Intelligenti per Internet, incentrato sull'Activity Recognition, di Davide Cassetta e Dalila Rosati. 

Prima di avviare il training occorre effettuare alcune operazioni sul dataset: 
avviare extract_frames.py dando come destinazione la cartella in cui risiedono i video, che hanno nomi sequenziali del tipo 1.mp4; extract_frames crea una cartella per ogni video e estrae i frame e li mette nelle cartelle create.

Avviare process_dataset.py che prende in input i file csv di train, validation, test e le cartelle dei frame e crea in output i file txt relativi, con l’indice del video, il numero dei frame e l’indice della categoria.
Fatto ciò è possibile avviare il training (sostituendo path_to_main con il path in cui risiede main.py) con il comando: 

python 'path_to_main/main.py' sport RGB \
                     --arch BNInception --num_segments 8  \
                     --consensus_type TRNmultiscale  --batch-size 64


Per il testing invece il comando è:

python 'path_to_test_models/test_models.py' sport RGB \
path_to_model/model/TRN_sport_RGB_BNInception_TRNmultiscale_segment8_best.pth.tar'  --arch BNInception --crop_fusion_type TRNmultiscale --test_segments 8 

Per il test su un singolo video:

python 'path_to_test_video/test_video.py' --arch BNInception --dataset sport --weight 'path_to_model/model/TRN_sport_RGB_BNInception_TRNmultiscale_segment8_best.pth.tar' --frame_folder 'path_to_dataset/dataset/sport/frame-video/298'.

In alternativa è possibile aprire il file dataset-train.ipynb (per il training) e dataset-test.ipynb (per il testing) e eseguire i comandi presenti nei file.
