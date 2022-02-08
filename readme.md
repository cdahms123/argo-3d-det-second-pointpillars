### argo-3d-det-second-pointpillars

#### steps to run:

#### 1) Download and Setup Argoverse Tracking

Make a directory `~/DownloadsArgoverse` and from https://www.argoverse.org/data.html under Argoverse 1.1 download the following:<br>

Under `Simple Datasets v1.1`:<br>
`3D Tracking` link (filename `tracking_sample_v1.1.tar.gz`)<br>
<br>
Under `Argoverse HD Maps`:<br>
`Miami and Pittsburgh` link (filename `hd_maps.tar.gz`)<br>
<br>
Under `Argoverse 3D Tracking v1.1`:<br>
`Training Part 1` link (filename `tracking_train1_v1.1.tar.gz`)<br>
`Training Part 2` link (filename `tracking_train2_v1.1.tar.gz`)<br>
`Training Part 3` link (filename `tracking_train3_v1.1.tar.gz`)<br>
`Training Part 4` link (filename `tracking_train4_v1.1.tar.gz`)<br>
`Validation` link (filename `tracking_val_v1.1.tar.gz`)<br>
`Testing` link (filename `tracking_test_v1.1.tar.gz`)<br>
<br>
Make a directory `~/argoverse-tracking` and extract/move/rearrange the above downloads into it so it ends up as follows:

```
~/argoverse-tracking
    /sample  (1 trip)
    /test    (24 trips)
    /train   (65 trips)
    /val     (24 trips)
```

Note the following:<br>
-after extracting, the folders with the trip data are nested multiple levels<br>
-the `train` directory has to be made and the trips from `train1`, `train2`, `train3`, and `train4` have to be moved into `train`<br>
-the `hd_maps.tar.gz` file (from the `Argoverse HD Maps` -> `Miami and Pittsburgh` link) is not used in this step, but rather is put inside the `argoverse-api` clone in the following steps.<br>

#### 2) Clone argoverse-api repository:

```
cd ~
git clone https://github.com/argoai/argoverse-api.git
```

#### 3) Download and move map files into clone

Extract the `hd_maps.tar.gz` file (from the `Argoverse HD Maps` -> `Miami and Pittsburgh` link), this will provide the directory `map_files`.  Move the extracted directory `map_files` inside the root of your `argoverse-api` clone.  When done, your `argoverse-api` directory structure should look like this:

```
~/argoverse-api
    /argoverse/...
    /demo_usage/...
    /docs/...
    /images/...
    /integration_tests/...
    /map_files/...        <-- this directory has to be manually added per the instructions above, all others are simply part of the clone
    /sphinx/...
    /tests/...
    /Argoverse-Terms_of_Use.txt
    /CONTRIBUTING.md
    /LICENSE
    /MANIFEST.in
    /pyproject.toml
    /README.md
    /setup.cfg
    /setup.py
    /tox.ini
    
```

#### 4) Install argoverse-api as a pip package

Note: The instructions for this step deviate from the https://github.com/argoai/argoverse-api readme instructions step 4, which I could not get to work.  These instructions involve making a copy of the map data into the pip package install location which is sloppy, but it works.

ToDo: Reconcile official instructions to these eventually.

```
cd ~/argoverse-api
sudo python3 setup.py install
sudo cp -R /home/cdahms/argoverse-api/map_files /usr/local/lib/python3.8/dist-packages/argoverse-1.1.0-py3.8.egg/
```

#### ToDo: write rest of this when content is complete


#### 999) Submit

Upload file to https://eval.ai/web/challenges/challenge-page/725/submission.

Check submission at https://eval.ai/web/challenges/challenge-page/725/my-submission.

When submission has processed, view leaderboard https://eval.ai/web/challenges/challenge-page/725/leaderboard/1974






