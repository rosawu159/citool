
image = "icl/docker-web"
container = "Web"
localpath="/home/icl/docker-storage/web"
path= ${localpath}":/home/user/"

image:
	docker build -t ${image} --network my-net .
run:
	mkdir -p ${localpath}
	docker run -dt --network my-net --name ${container} -v${path} ${image}
exec:
	docker exec -it ${container} bash

clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}

