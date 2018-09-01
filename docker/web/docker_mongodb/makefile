image = "icl/docker-mongodb"
container = "Mongodb_container"
user="mongodb_user"
localpath="/home/icl/docker-storage/Web/db"
path= ${localpath}:"/data"
port="27017:27017"

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

