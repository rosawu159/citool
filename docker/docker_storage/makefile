
image = "icl/docker-storage"
container = "Storage"
path= "/home/icl/docker-storage:/data"
jenkpath=${path}/jenkins
image:
	docker build -t ${image} --network my-net .
run:
	docker run -dt --network my-net --name ${container}  -v ${path} ${image}
start:
	docker create --network my-net --name ${container}  -v ${path} -v ${jenkpath} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}
cleani:
	docker rmi ${image}

