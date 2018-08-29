image = "icl/docker-mongodb"
container = "MongoDB"
user="mongodb_user"
localpath="/home/icl/docker-storage/mongodb"
path= ${localpath}":/home/"$user
port="27017:38383"

image:
	docker build -t ${image} --network my-net .
run:
	mkdir -p ${localpath}
	docker run -dt --network my-net --name ${container} -p ${port} -v${path} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}

