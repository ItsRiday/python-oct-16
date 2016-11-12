todo=[,]
done=[,]
for x  in range(100000000000000000000000000000000)
	print you have to do these tasks 
	print todo
	print you have done these tasks
	print done
	addtask=raw_input("add a task to do.If you don't want to, then just hit enter")
	todo.append(addtask)
	removetask=raw_input("remove a task you have done.If you don't want to, then just hit enter")
	todo.remove(removetask)
	done.append(removetask)
