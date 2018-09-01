image = "icl/docker-android"
container = "Android_container"
path= "/home/icl/docker-storage/Android:/data"
vncPort="5900:5900"

image:
	docker build -t ${image} --network my-net .
run:
	docker run -dt --network my-net -p ${vncPort} -p"5901:5901" --name ${container} -v ${path} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}

