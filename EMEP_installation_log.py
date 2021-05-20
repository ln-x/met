
cd $DATA/src/EMEP
git clone --branch development https://github.com/pacedproton/WRF_environment_installation.git #for metHPC:
git clone --branch master https://github.com/pacedproton/WRF_environment_installation.git #for VSC:
#change worf.sh:
export PREFIX=/gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build

bash worf.sh |& tee build.log
cd /gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/pkg-src/wrf
source /gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/wrf_environment.sh
#./configure
#select DMPAR - Intel (15)
#edit configure.wrf, e.g. with
#        DM_FC=mpiifort
#        DM_CC=mpiicc

#compile model with e.g. ./compile <model name>
# for WRF-chem: additionally issue ./compile emi_conv
#    issue ./clean before making changes to recompile or clean -a which also overwrites configure.wrf

#https://emep-ctm.readthedocs.io/en/latest/Intro.html#getting-started
wget https://raw.githubusercontent.com/metno/emep-ctm/tools/catalog.py
chmod +x catalog.py
./catalog.py -R rv4_36 --source

#Changes im Makefile
INCL= -I/gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/netcdf_c/include -I/gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/netcdf_f/include
LIB= -L/gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/netcdf_c/lib -L/gpfs/data/fs71449/htrimmel3/src/EMEP_WRF_libs20210520/build/0520/netcdf_f/lib

mpiifort (statt mpif90)

#handy keyboard shoartcuts: ctr+z, fg, bg


#!/bin/bash
cd ~/work/EMEP_MSC-W_model.rv4.36.OpenSource/Base
mpprun   ../code/emepctm # depending on the HPC/queue


