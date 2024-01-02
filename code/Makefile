all: seq eigen omp mpi

seq:
	make -f makefile.seq

eigen:
	make -f makefile.eigen

omp:
	make -f makefile.omp

mpi:
	make -f makefile.mpi
	
clean:
	rm -fv bin/*.o bin/*.exe
