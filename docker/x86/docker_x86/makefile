image = "icl/docker-x86"
container = "Android_X86_container"
#user="android_x86_user"
localpath="/home/icl/docker-storage/Android_x86"
path= ${localpath}:"/data"

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

