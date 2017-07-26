FC=gfortran -Wall -Wno-tabs 
BIN_DIR=bin
SCR_DIR=src
OUT_DIR=output

all: setup zdotbl.x zinv.x eiginv.x

zdotbl.x: $(SCR_DIR)/zundle_dp_bl.f90 setup
	$(FC)  $< -o $(BIN_DIR)/$@

zinv.x:$(SCR_DIR)/zundleinv.f90 setup 
	$(FC)  $< -o $(BIN_DIR)/$@ 

eiginv.x:$(SCR_DIR)/eigeninv.f90 setup 
	$(FC)  $< -o $(BIN_DIR)/$@ 

setup:
	mkdir -p $(BIN_DIR)
	mkdir -p $(OUT_DIR)
	mkdir -p plots_output

run: zdotbl.x zinv.x eiginv.x
	for file in `ls data/Zundel_Cation/traj/`; do \
		./$(BIN_DIR)/zdotbl.x data/Zundel_Cation/traj/$$file ;\
		./$(BIN_DIR)/zinv.x data/Zundel_Cation/traj/$$file ;\
	done 
	for file in `ls data/Eigen/traj/`; do \
		./$(BIN_DIR)/eiginv.x data/Eigen/traj/$$file ;\
	done 
		
plot: $(OUT_DIR)/dotp/*.dat
	for file in `ls $(OUT_DIR)/dotp/`; do \
		python src/plot.py $(OUT_DIR)/dotp/$$file ;\
	done 
	for file in `ls $(OUT_DIR)/inv1/`; do \
		python src/plot.py $(OUT_DIR)/inv1/$$file ;\
	done 
	for file in `ls $(OUT_DIR)/eiginv/ | grep \.dat`; do \
		python src/plot.py $(OUT_DIR)/eiginv/$$file ;\
	done 
	for file in `ls data/Eigen/ener/`; do \
		python src/plot.py data/Eigen/ener/$$file ;\
	done 


flush:
	rm -rf plots_output/* output/*
	
clean:
	rm -rf $(BIN_DIR) $(OUT_DIR) plots_output
