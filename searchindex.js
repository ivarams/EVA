Search.setIndex({envversion:50,filenames:["api/baseadapter","api/baseexecutor","api/config","api/eva","api/eventloop","api/eventqueue","api/exceptions","api/index","configuration","development","index","intro","metrics","restapi","tutorial","variables"],objects:{"":{eva:[3,0,0,"-"]},"eva.base":{adapter:[0,0,0,"-"],executor:[1,0,0,"-"]},"eva.base.adapter":{BaseAdapter:[0,1,1,""]},"eva.base.adapter.BaseAdapter":{adapter_init:[0,2,1,""],api:[0,3,1,""],blacklist_add:[0,2,1,""],clear_required_uuids:[0,2,1,""],concurrency:[0,3,1,""],create_job:[0,2,1,""],create_logger:[0,2,1,""],datainstance_has_required_uuids:[0,2,1,""],default_resource_dictionary:[0,4,1,""],executor:[0,3,1,""],expiry_from_hours:[0,2,1,""],expiry_from_lifetime:[0,2,1,""],finish_job:[0,2,1,""],forward_to_uuid:[0,2,1,""],generate_and_post_resources:[0,2,1,""],generate_resources:[0,2,1,""],has_output_lifetime:[0,2,1,""],has_productstatus_credentials:[0,2,1,""],init:[0,2,1,""],is_blacklisted:[0,2,1,""],is_in_required_uuids:[0,2,1,""],post_resources:[0,2,1,""],post_to_productstatus:[0,2,1,""],reference_time_threshold:[0,2,1,""],remove_required_uuid:[0,2,1,""],require_productstatus_credentials:[0,2,1,""],resource_matches_hash_config:[0,2,1,""],resource_matches_input_config:[0,2,1,""],validate_resource:[0,2,1,""]},"eva.base.executor":{BaseExecutor:[1,1,1,""]},"eva.base.executor.BaseExecutor":{abort:[1,2,1,""],create_temporary_script:[1,2,1,""],delete_temporary_script:[1,2,1,""],execute_async:[1,2,1,""],sync:[1,2,1,""]},"eva.config":{ConfigurableObject:[2,1,1,""],ResolvableDependency:[2,1,1,""],SECRET_CONFIGURATION:[2,7,1,""],resolved_config_section:[2,5,1,""]},"eva.config.ConfigurableObject":{CONFIG:[2,3,1,""],OPTIONAL_CONFIG:[2,3,1,""],REQUIRED_CONFIG:[2,3,1,""],_factory:[2,2,1,""],config_id:[2,3,1,""],factory:[2,6,1,""],format_config:[2,2,1,""],init:[2,2,1,""],isset:[2,2,1,""],load_configuration:[2,2,1,""],normalize_config_bool:[2,4,1,""],normalize_config_config_class:[2,4,1,""],normalize_config_int:[2,4,1,""],normalize_config_list:[2,4,1,""],normalize_config_list_int:[2,4,1,""],normalize_config_list_string:[2,4,1,""],normalize_config_null_bool:[2,4,1,""],normalize_config_positive_int:[2,4,1,""],normalize_config_string:[2,4,1,""],resolve_dependencies:[2,2,1,""],set_config_id:[2,2,1,""]},"eva.config.ResolvableDependency":{resolve:[2,2,1,""]},"eva.eventloop":{Eventloop:[4,1,1,""]},"eva.eventloop.Eventloop":{adapter_by_config_id:[4,2,1,""],assert_event_matches_object_version:[4,2,1,""],create_event_queue_timer:[4,2,1,""],create_job_for_event_queue_item:[4,2,1,""],create_jobs_for_event_queue_item:[4,2,1,""],drained:[4,2,1,""],draining:[4,2,1,""],graceful_shutdown:[4,2,1,""],handle_kafka_error:[4,2,1,""],initialize_event_queue_item:[4,2,1,""],initialize_job:[4,2,1,""],instantiate_productstatus_data:[4,2,1,""],job_by_id:[4,2,1,""],main_loop_iteration:[4,2,1,""],must_the_show_go_on:[4,2,1,""],next_event_queue_item:[4,2,1,""],notify_job_failure:[4,2,1,""],notify_job_success:[4,2,1,""],poll_listeners:[4,2,1,""],process_all_in_product_instance:[4,2,1,""],process_data_instance:[4,2,1,""],process_job:[4,2,1,""],process_next_event:[4,2,1,""],process_rest_api:[4,2,1,""],reinitialize_job:[4,2,1,""],report_event_queue_metrics:[4,2,1,""],report_job_status_metrics:[4,2,1,""],reset_event_queue_item_generator:[4,2,1,""],restart_listeners:[4,2,1,""],restore_queue:[4,2,1,""],set_drain:[4,2,1,""],set_health_check_heartbeat_interval:[4,2,1,""],set_health_check_heartbeat_timeout:[4,2,1,""],set_health_check_skip_heartbeat:[4,2,1,""],set_health_check_timestamp:[4,2,1,""],set_message_timestamp_threshold:[4,2,1,""],set_no_drain:[4,2,1,""],shutdown:[4,2,1,""]},"eva.eventqueue":{EventQueue:[5,1,1,""],EventQueueItem:[5,1,1,""]},"eva.eventqueue.EventQueue":{adapter_active_job_count:[5,2,1,""],add_event:[5,2,1,""],delete_stored_item:[5,2,1,""],empty:[5,2,1,""],get_stored_queue:[5,2,1,""],init:[5,2,1,""],item_keys:[5,2,1,""],remove_item:[5,2,1,""],status_count:[5,2,1,""],store_item:[5,2,1,""],store_list:[5,2,1,""],store_serialized_data:[5,2,1,""],zk_get_serialized:[5,2,1,""],zk_get_str:[5,2,1,""],zk_immediate_store_disable:[5,2,1,""],zk_immediate_store_enable:[5,2,1,""]},"eva.eventqueue.EventQueueItem":{add_job:[5,2,1,""],empty:[5,2,1,""],failed_jobs:[5,2,1,""],finished:[5,2,1,""],id:[5,2,1,""],job_keys:[5,2,1,""],remove_job:[5,2,1,""],serialize:[5,2,1,""],set_adapters:[5,2,1,""]},"eva.exceptions":{AlreadyRunningException:[6,8,1,""],ConfigurationException:[6,8,1,""],DuplicateEventException:[6,8,1,""],EvaException:[6,8,1,""],EventTimeoutException:[6,8,1,""],GridEngineParseException:[6,8,1,""],InvalidConfigurationException:[6,8,1,""],InvalidEventException:[6,8,1,""],InvalidGroupIdException:[6,8,1,""],InvalidRPCException:[6,8,1,""],JobNotCompleteException:[6,8,1,""],JobNotGenerated:[6,8,1,""],MissingConfigurationException:[6,8,1,""],MissingConfigurationSectionException:[6,8,1,""],RPCException:[6,8,1,""],RPCFailedException:[6,8,1,""],RPCInvalidRegexException:[6,8,1,""],RPCWrongInstanceIDException:[6,8,1,""],ResourceTooOldException:[6,8,1,""],RetryException:[6,8,1,""],ShutdownException:[6,8,1,""],ZooKeeperDataTooLargeException:[6,8,1,""]},eva:{coerce_to_utc:[3,5,1,""],config:[2,0,0,"-"],convert_to_bytes:[3,5,1,""],epoch_with_timezone:[3,5,1,""],eventloop:[4,0,0,"-"],eventqueue:[5,0,0,"-"],exceptions:[6,0,0,"-"],format_exception_as_bug:[3,5,1,""],import_module_class:[3,5,1,""],in_array_or_empty:[3,5,1,""],log_productstatus_resource_info:[3,5,1,""],netcdf_time_to_timestamp:[3,5,1,""],now_with_timezone:[3,5,1,""],print_and_mail_exception:[3,5,1,""],retry_n:[3,5,1,""],split_comma_separated:[3,5,1,""],strftime_iso8601:[3,5,1,""],url_to_filename:[3,5,1,""],zookeeper_group_id:[3,5,1,""]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","staticmethod","Python static method"],"5":["py","function","Python function"],"6":["py","classmethod","Python class method"],"7":["py","data","Python data"],"8":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:staticmethod","5":"py:function","6":"py:classmethod","7":"py:data","8":"py:exception"},terms:{"0fmkdgp":13,"1vlcf9h":13,"2a6af9dhiic":[],"2xx":13,"31t":[],"4pgu7disrx4bbvm0b4":13,"6joa0jh9ul9lcvx30qgpt":13,"7dfb76z9blritlb3ugb0ly":[],"7hvkdlokgkv37jh0":[],"7vj":13,"7xtifhga6dllbq8j":[],"8ttxswyspm":13,"90abcdef":13,"abstract":[],"boolean":2,"byte":[3,12],"case":[4,5,8],"catch":3,"class":[],"const":[],"default":[0,2,8,14,15],"delete":13,"export":[],"final":2,"float":3,"import":[0,3,9,14],"int":[0,2,3],"long":[0,3],"new":[0,4,14,15],"null":[0,3],"return":[0,1,2,3,4,5],"static":[0,2],"throw":[2,3,5],"transient":[6,12],"true":[0,2,3,4,5,8,14,15],"try":[2,6],"var":[],"while":[2,5,13],__init__:3,_count:12,_factori:2,_size:12,abil:8,abl:0,abort:[1,12],about:[0,3,4,8,14],abov:13,absolut:0,accept:[0,4,8,11,12,13,14],access:14,accord:[2,6,14],across:[],action:0,activ:[5,9],actual:14,acymdeptrkvaaffya0hwxetijcexvuuf6aqvzyk6fo8f8qx4o:[],adapt:[],adapter_:[],adapter_active_job_count:5,adapter_by_config_id:4,adapter_init:[0,14],adaptive:[],add:[0,5,6,8],add_ev:5,add_job:5,adding:[],addit:5,advanc:8,after:[0,1,2,4,6,12,14],afterward:1,again:[3,4,12],against:[0,12],agent:13,aihsec7:13,algorithm:14,aliv:13,all:[],allow:[2,13],along:[2,13],alreadi:[2,5,6,12],alreadyrunningexcept:6,also:[0,13],alwai:15,anatomi:[],ani:[0,2,4,12,13,14],anoth:[8,15],any:3,anyth:3,anywai:[],api_kei:2,appear:[],appli:15,applic:[8,13],apt:9,arg:3,argument:[3,13],around:5,arrai:[0,3],arriv:[6,12,14],ask:4,assert:[2,14],assert_event_matches_object_vers:4,assertionerror:[3,4],associ:[5,14],assum:[8,14],asynchron:[1,4,11],attack:13,attempt:12,attr:[],attribut:14,authent:13,author:13,automat:[],avail:[2,11,13],avoid:8,awar:3,awk:14,ayob2i99:[],back:[0,14],backend:[0,8],backtrac:3,bar:[2,15],bare:14,base:[],baseadapt:[0,4,5,14],baseexecutor:1,basename:2,basic:[8,13,14],baz:2,becaus:[6,9,12],been:[0,2,4,5,6,8,13],befor:[0,3,12],begin:13,behavior:[],belong:[4,12],below:2,between:[3,4],bg9szmfjztphymm:13,big:[6,8],bin:[9,13,14],blacklist:0,blacklist_add:0,blacklist_uuid:[],blah:[],blrewhuxqywyjkxs77vmkp59bbtlnh153bzlbjulvmab:13,bool:[0,2,3],both:8,brief:[0,1,4,5],broker:12,bug:[2,6],buggi:13,build:9,cach:[12,14],calcul:0,call:[0,2,3,5,6,14],caller:3,can:[0,2,3,4,5,8,13,14],cannot:6,censor:2,certain:13,chang:[0,12,14],charset:13,check:[],checksum:[0,14],checksumadapt:14,checksumverificationadapt:12,child:[0,4],children:0,chronograph:11,chronolog:[],circumst:6,classmethod:2,clean:[1,3],clear_required_uuid:0,client:[],clobber:9,clone:9,code:[],coerc:[],coerce_to_utc:3,collect:5,com:[8,9],combin:2,come:11,comma:[2,3,8],command:[6,8,11,13,14],comment:8,commit:12,compil:[],complain:14,complet:[1,6,14],compon:[0,3],comput:14,concern:14,concurr:0,config:[],config_class:[0,2],config_class_:[],config_id:[2,4],configpars:[2,6],configur:[],configurableobject:[0,2,14,15],configurationexcept:6,connect:[5,8,12,13],constant:[],contain:[],content:[],contextu:[],continu:4,control:13,conveni:0,convers:[3,13],convert:[0,2,3],convert_to_byt:3,copi:3,correct:11,correctli:[0,13],cost:14,could:12,count:4,counter:12,counterpart:12,cpython:13,crash:[5,12],creat:[],create_event_queue_tim:4,create_job:[0,14],create_job_for_event_queue_item:4,create_jobs_for_event_queue_item:4,create_logg:0,create_temporary_script:1,credenti:0,criteria:[0,6],cross:8,current:[0,3,4,5,11,15],custom:[0,9,14],cw2jmlpzf9sljwlep5zkl8uhqbtg:13,daemon:[],data:[0,2,4,5,6,12,13,14],data_inst:[],data_instance_uuid:4,databas:14,datainst:[0,4,12,14],datainstance_has_required_uuid:0,dataset:[],date:13,datetim:[0,3],dbzf4009es1a4nmyykqrs4w4ekiljsd:[],debug:5,dec:13,def:14,default_resource_dictionari:0,defin:[0,2,3,4,8,14,15],definit:[2,8],deflat:13,degre:13,delai:[],delet:[0,5,12],delete_stored_item:5,delete_temporary_script:1,deleteadapt:12,delimit:8,deliveri:14,dep:9,depend:9,deprecated:0,deriv:[0,2,15],describ:14,descript:[0,12],detach:13,detail:[],detect:5,determin:0,dev:9,dict:[2,3,5],dictionari:[0,2,5,14],did:[6,12],differ:[2,4],direct:[],directli:11,directori:[8,9,14],disabl:5,disabled:14,discard:12,displai:[],doc:9,docker:[],doe:[0,2,3,6],done:13,dot:[2,3,15],down:4,drain:[4,13],driven:14,due:[6,14],duplic:[0,8],duplicateeventexcept:[5,6],e6alrmuvpqmpzckio8chrgcbhm6dm:13,each:[4,5,14],earlier:[],either:[0,3,4,8,9,12,14,15],elif:14,els:[13,14],email:4,empti:[0,3,4,5],empty:2,enabl:[4,5,8,13,14],encode:13,end:[8,13],engin:1,ensur:5,entir:8,entri:5,env:[2,14],environ:[],environment_vari:[],ephemer:5,epoch_with_timezon:3,error:[2,3,4,5,6,11,12,13],escal:3,eva:[],eva_adapter_count:12,eva_deleted_datainst:12,eva_event_accept:12,eva_event_dupl:12,eva_event_heartbeat:12,eva_event_productstatu:12,eva_event_queue_count:12,eva_event_receiv:12,eva_event_reject:12,eva_event_too_old:12,eva_event_version_unsupport:12,eva_input_with_hash:[],eva_job_failur:12,eva_job_status_chang:12,eva_job_status_count:12,eva_kafka_commit_fail:12,eva_kafka_no_brokers_avail:12,eva_md5sum_fail:12,eva_queue_order:[],eva_recoverable_except:12,eva_requeue_reject:12,eva_requeued_job:12,eva_resource_object_version_too_old:12,eva_restored_ev:12,eva_restored_job:12,eva_shutdown:12,eva_start:12,eva_zk_:12,eva_zookeeper_connection_loss:12,evaexcept:6,evaluatedresourc:0,event_uuid:5,eventqueu:[],eventqueueitem:[4,5],events_:[],eventtimeoutexcept:6,everi:[14,15],everyon:14,evid:14,exactli:[],exampl:[8,13,15],exampleadapt:8,except:[],exception:[],excruci:14,execut:[],execute_async:1,executor:[],exist:[2,3,5,6],exit:11,expect:[4,6,14],expiri:0,expiry_from_hour:0,expiry_from_lifetim:0,explan:8,explicit:0,expos:13,express:6,extern:2,factori:2,fail:[4,5,6,14],failed_job:5,failur:[3,4,5,12],fall:14,fals:[0,2,3,4,5],fast:4,faster:[],featur:13,few:15,fifo:[],file:[],filenam:0,filesystem:12,fill:1,filter:2,find:8,finish:[0,4,5,9,14],finish_job:[0,14],first:[8,14,15],fit:6,flag:0,flow:14,follow:[0,5,13,15],foo:[2,8,15],fooadapt:15,foobar:15,forev:0,format:[],format_config:2,format_exception_as_bug:3,format_help:[],forth:[0,8],forward:4,forward_to_uuid:0,found:[2,3,4],from:[0,2,3,4,5,6,8,11,12,14,15],full:[1,3,15],func:3,further:11,furthermor:13,futur:2,gaug:12,generate_and_post_resourc:0,generate_resourc:[0,14],get:[1,9,13],get_stored_queu:5,gigabyt:3,git:9,github:9,give:[3,4],give_up:3,given:[0,4],global:[8,15],gmt:13,gnupg:13,gpg:13,gpg_key_id:13,grace:4,graceful_shutdown:4,grant:8,grib:8,grid_engin:8,gridengin:6,gridengineexecutor:8,gridengineparseexcept:6,group:8,group_id:6,guarante:[0,2,5],gzip:13,had:12,handl:[5,13,14],handle_kafka_error:4,has_output_lifetim:0,has_productstatus_credenti:0,hash:[0,2,14],hash_command:14,hash_typ:14,have:[0,2,5,8,12,14],header:13,health:[],health_check_serv:[],healthi:4,heartbeat:[4,12],help:[9,13,14],here:[0,8,14],highli:11,hmyosw1ebt:13,home:8,host:[8,13],hour:0,how:[0,3,12,14],hp0apowl:13,http:[],httpie:[],i7bzpg0tgtshhqp:13,id_rsa:8,identifi:[],ignor:[0,2,8],ignore_default:2,immedi:[1,4],implement:[0,2],impli:8,implicit:8,import_module_class:3,in_array_or_empti:3,includ:[],inclus:14,inclusion:0,incom:0,incompat:6,incub:[2,8],indefinit:3,index:10,indic:2,individu:5,infinit:2,info:14,inform:[0,3,5,8,14],infrastructur:[11,14],inherit:[0,8,15],ini:[2,8,14],init:[0,2,5],initi:[0,2,4,5,14],initial:[0,14],initialize_event_queue_item:4,initialize_job:4,input:[0,2,11],input_:0,input_data_format:0,input_file_format:8,input_parti:0,input_product:[0,15],input_reference_hour:0,input_service_backend:[0,8],input_with_hash:0,insid:14,instal:9,instanc:[0,2,3,4,5,6,13,14],instance_id:6,instanti:[2,4,8,12,15],instantiat:[0,2,5,14],instantiate_productstatus_data:4,instead:3,instruct:[0,11],insuffici:14,integ:2,interest:14,interfac:11,intern:[8,12],interv:[3,4],introduct:[],introduction_:[],invalid:[2,6],invalidconfigurationexcept:[2,6,14],invalideventexcept:6,invalidgroupidexcept:[3,6],invalidrpcexcept:6,iqicbaabagagbqjyv6cfaaojeijrrk:[],iqicbaabagagbqjyv7nhaaojeijrrk:13,irrecover:12,irrevers:[],is_blacklist:0,is_in_required_uuid:0,iso8601:3,isset:2,item:[4,5,12],item_id:5,item_kei:5,iter:[4,5],itself:9,ixhxkayfbklemo26xf:[],job:[],job_by_id:4,job_id:5,job_kei:5,job_uuid:5,jobnotcompleteexcept:6,jobnotgener:6,join:[14,15],jqzre:13,json:[5,13],k2ebghpd:13,k3iftkzxfbapmdvtlfzet8lcretfv93zfe7rrsyfvcxygc9h6doeskwx53edyuej:13,kafka:[4,11,12,13],kazoo:5,keep:13,kei:[0,2,13],keyword:3,kicxhqkmk9xlxfgqtjxblge5oyewh:[],kilobyt:3,kind:12,know:[],kq4zs8vthurjifcacnszmuqb3xp7gti:[],ktapdvimxlo:13,kwarg:3,kxqqcoridj87j:13,lack:[],laip:13,larg:5,last:[],later:14,latest:[],latter:[],lax1ivuloyknt8yajjjlx2k:[],leav:4,length:13,let:[8,14],level:8,lftjrdclhk4:13,lib:3,lifetim:0,lifo:[],like:[8,14],line:[3,8,14],list:[0,2,3,4,5],list_int:[0,2],list_str:0,list_string_:[],listen:[4,8,14],live:[0,14],load:[],load_configur:2,load_serialized_data:[],local:9,localhost:[8,13],locat:8,log:[0,2,3,4,5,11],log_productstatus_resource_info:3,logger:[0,3],logic:[11,14],loglevel:3,lol:[],look:[2,8,14],loop:4,loss:12,lost:[3,12,13],lot:4,lsx02yhqqk1e6sotsmjaxe6se3dob48n:13,lytfqehvobyfdc0fao8hfpnjh9sb:13,machin:9,made:[2,13],mai:[0,2,4,13,14,15],mail:[3,4,8],mailer:[3,8],main:[4,11,14],main_loop_iter:4,maintain:[4,5],make:[4,6,9,11,13,14],manag:5,mani:[0,3,8],mark:[0,12,14],match:[0,4,6,12],mbswtd5opp8mikweluasossbf:[],md5:14,md5sum:[12,14],mean:[0,13,14],meaning:[0,14],measur:4,megabyt:3,memb:[],member:[2,3],merg:8,messag:[0,3,4,5,6,11,12,13,14],metadata:[],method:[2,5,14],metno:9,metric:[],metric_bas:5,might:[2,4],minim:0,minimum:14,mirror:5,misbehav:13,mismatch:12,miss:[2,6],missingconfigurationexcept:[2,6],missingconfigurationsectionexcept:[2,6],mnbu580jx73nhy1w0f:13,model:[],modifi:14,modul:[],mon:13,monitor:13,more:[4,6,8,12],most:[0,8],much:4,multipl:[],must:[0,2,5,8,13,14,15],must_the_show_go_on:4,myclass:2,name:[0,2,3,8,15],ncdump:3,neccessari:14,necessari:[2,5],need:[2,4,6,14],netcdf:8,netcdf_time_to_timestamp:3,network:[6,12],never:0,newer:[],newli:[0,14],next:[6,14],next_event_queue_item:4,njrd:[],node:14,non:4,none:[0,2,4,5],noob:[],normal:2,normalize_config_:2,normalize_config_bool:2,normalize_config_config_class:2,normalize_config_int:2,normalize_config_list:2,normalize_config_list_int:2,normalize_config_list_str:2,normalize_config_null_bool:2,normalize_config_positive_int:2,normalize_config_str:2,nosetest:[],notat:[3,15],note:[2,5,8,14],noth:[0,2,14],notifi:4,notify_job_failur:4,notify_job_success:4,now:14,now_with_timezon:3,nr53:13,nrlxhwppy2mq3tpt:[],null_bool:0,null_bool_:[],null_str:3,nullabl:2,number:[0,3,4,5,14],nvtzj26et1sp4qa3rctazoqgeidngo48wt:13,nxjsr1xs4jb:13,object:[0,2,3,4,5,6,13,14],object_:2,offici:8,ofo:[],older:[0,12],oldest:0,omit:14,omytkhrtmho8t33cgdytilcehaf5sj0:[],onc:[0,2,4],once:0,onli:[],only:[0,15],opengridengin:[],oper:[0,6],option:[0,2,14,15],optional:2,optional_config:[2,14],order:[0,2,4,5,8,11,14],ordereddict:5,origin:[12,14],other:[8,12,13,15],otherwis:[0,4,5,15],our:[6,14],out:[2,4,9],outag:6,outdat:6,output:[0,2,3,6,11,14],output_base_url:0,output_data_format:0,output_filename_pattern:0,output_lifetim:0,output_product:0,output_service_backend:[0,8],outsid:14,over:11,overrid:[2,14],overwrit:[],overwritten:6,own:[0,2,4,5,8,12,15],packag:9,page:10,pair:8,param:[0,1,2,5,14],paramet:[0,2,3,4,5,8,14],parent:0,parm:[],pars:[2,3,6],parse_boolean_str:[],parser:2,part:[11,14,15],partial:0,particular:5,pass:[3,14],patch:13,path:[1,3,5,8,14],pattern:0,payload:[5,13],pend:12,perform:[0,6],period:6,perman:14,persist:14,pgp:13,pid:5,pip:9,place:[0,2,14],pleas:8,point:2,poll:4,poll_listen:4,popul:[0,2,4,5,14],port:[8,13],posit:[2,3,12],positive_int:0,possibl:2,post:[0,13,14],post_resourc:0,post_to_productstatu:0,pre:[2,3],presed:[],present:[8,12],prevent:13,previou:[8,12],previous:4,primari:0,print:[3,14],print_and_mail_except:3,probabl:[13,14],proce:[2,9],process:[0,3,4,5,6,11,12,13,14],process_all_in_product_inst:4,process_data_inst:4,process_health_check:[],process_job:4,process_next_ev:4,process_parti:[],process_rest_api:4,process_rpc_ev:[],product:[0,11],product_inst:[],product_instance_uuid:4,productinst:[0,4],productstatu:[],productstatuslisten:8,productstatusresourceev:4,program:[4,5,9,12,14,15],proper:5,properti:11,protect:2,protocol:12,provid:[0,2,5,11,13],publicli:13,pull:2,put:[13,14],pvqvp55:13,python3:[3,13],python:[3,8,9,11,13,14,15],qfb1tag:[],qu6dmvrtqhrry29wzxiig:13,queri:13,queu:12,queue:[4,5,6,11,12,13,14],quickli:4,r5vhzqowijmv:13,rais:[0,2,3,4,14],raw:5,read:[],reason:14,receiv:[4,5,6,8,11,12],recent:6,recipi:8,recommend:9,reconstruct:5,recov:4,recurs:[2,8],refer:[0,2,4,5,6,8,15],referenc:8,reference_time_threshold:0,refus:15,regard:2,regardless:[12,14,15],registri:9,regular:[4,6],regularli:12,reimplement:2,reiniti:4,reinitialize_job:4,reject:[12,13],relat:[5,6],remov:[1,5],remove_item:5,remove_job:5,remove_required_uuid:0,render:[8,15],replac:2,replai:13,repond:13,report:[],report_event_queue_metr:4,report_job_status_metr:4,repositori:14,repres:[0,3],represent:[2,5],request:[],requir:[0,2,8,14],require_productstatus_credenti:0,required_config:2,required_uuid:0,reset:4,reset_event_queue_item_gener:4,resolv:[2,8],resolvabledepend:2,resolve_depend:2,resolved_config_sect:2,resourc:[0,3,4,6,12,14],resource_matches_hash_config:0,resource_matches_input_config:0,resourcetoooldexcept:[4,6],respons:[0,4],rest:[],rest_api_serv:4,rest_serv:[8,13],restart:[],restart_listen:4,restor:12,restore_queu:4,result:[4,6,12,14],retri:[3,14],retriev:[4,5,14],retry_n:3,retryexcept:[6,14],revers:[],right:14,rjp:[],rnyxal4ckovgk1:[],robust:11,root:15,rpc:[],rpcexception:6,rpcfailedexcept:6,rpcinvalidregexexcept:6,rpcwronginstanceidexcept:6,rtquie2outjhaixrf3a83qtetaump8cpjty31dgalztuzsy6isdzoxi:13,rtype:[],run:[],runtimeerror:[2,3,5],rxy74nyf0ntvuxjmwotr2c4xwn2mbkbqj10nnixwejrsm16gmjr6fckzdf9syv:[],s1we58xh:13,sake:14,same:5,saniti:0,save:[4,14],scan:8,schedul:[4,11,14],script:[1,14],sd0fczwg6rukvqtr8vjpnxhac946aml:[],search:[4,10],second:[0,4,13,14],secret_configuration:2,section:[],section_kei:2,see:[0,2,8,12,14],self:[0,14],selv:14,send:[3,4],send_email:[],sens:[6,11],sensit:13,sent:[3,6,13,14],separ:[2,3,5],sequenti:4,serial:[4,5,12],server:[4,8,12,13],servic:[0,6],servicebackend:[],set:[],set_adapt:5,set_config_id:2,set_drain:4,set_health_check_heartbeat_interv:4,set_health_check_heartbeat_timeout:4,set_health_check_skip_heartbeat:4,set_health_check_timestamp:4,set_message_timestamp_threshold:4,set_no_drain:4,setup_process_parti:[],setup_reference_time_threshold:[],sever:[],sha256:14,sha256sum:14,shall:2,shell:[],shelladapt:[],ship:13,should:[0,1,4,5,6,8,11,14,15],show:14,shut:4,shutdown:[4,12],shutdownexcept:6,sigint:6,signal:[6,13],signatur:13,signature:13,sigterm:6,similar:8,simplic:14,simplifi:13,singl:[0,2,3,4,6],size:3,skeleton:14,skip:4,small:11,smtp_host:8,snip:[],some:12,someth:14,soon:[2,5],sort:[],sourc:[0,1,2,3,4,5,6,9,14],special:15,specif:[4,5,11,12],specifi:[0,1,2,8,14,15],split:[2,3],split_comma_separ:3,src:[],ssh:8,ssh_host:8,ssh_key_fil:8,ssh_user:8,standard:[11,14],start:[0,1,3,8,12,13,14,15],startup:[8,12],state:[1,12],statsd:[4,8,12],statu:[1,4,5,12,13],status_count:5,stdout:14,step:[],stop:4,storag:[5,11],store:[0,5,6,12,14],store_item:5,store_list:5,store_serialized_data:5,str:[2,3,4,5],strftime_iso8601:3,string:[0,2,3,5,8,14],strip:14,structur:[5,8,11],style:[],subclass:[0,2],subject:[],submit:[],successfulli:4,sudo:9,suffici:0,suitabl:[3,5],sun:[],support:[13,14],sure:[4,11],sync:1,syntax:[],system:[9,11,13,14],t9w4loznmlqwlqruoki5yfwrx6n:[],tag:12,take:[0,4,14],task:[0,11],tbd:[],tell:4,templat:0,temporari:1,terabyt:3,termin:14,test:[],text:[],than:[0,2,12,15],thei:[0,2,5,8,11,14],them:[2,4],themselv:0,thi:[0,2,4,5,6,8,9,13,14,15],thing:14,those:[],thread:[],three:[11,14],threshold:12,through:[0,4,13],thrown:[5,6],thu:[5,14],time:[0,3,4,6,12,13,14],time_str:3,timedelta:[],timeout:4,timer:4,timestamp:[3,4,12],timezon:3,tjygv3lcur9:[],toler:3,too:[4,5,6],tool:13,top:8,total:5,touch:5,translat:[],transport:11,treat:6,trigger:11,tupl:[2,3],tutori:[],two:[2,8,14],type:[0,2,3,4,12,13,14],typic:6,ubmo3i1zsiwttghtabcybvfv8omyz1xkr9hyor5gtdrgz8qhuns26hznwy7cd:[],ubqrdm:[],ultim:11,under:[5,6,15],underli:6,unexpect:6,unfinish:4,unicod:2,uniqu:8,unseri:5,unset:0,unv34bsgr:[],updat:[12,14],upload:9,upon:[8,12,14],uqsscfx14mkfq:[],uri:4,url:[0,3,8,14],url_to_filenam:[3,14],usabl:14,usage:2,use:[5,15],used:5,user:[0,8,13,14],usr:3,usual:5,utc:3,utf:13,util:11,uuid:[0,4],v6rt5fyjuvjgxlin7:[],valid:[0,4,6,14],validate_resourc:0,valu:[0,2,3,8,14],valueerror:3,variabl:[],variable:0,variou:6,verifi:14,version:[4,12,13],via:4,virtualenv:9,wai:12,wait:3,want:[3,5,9,14],warn:3,warning:[3,14],wehyzq3x7xvh81cflk7:[],well:[3,5],were:[5,12],what:[],when:[2,3,4,5,6,8,13,14,15],where:[0,3,8],whether:[0,2,14],which:[0,2,4,5,13,14],whitespac:8,who:14,whose:0,wide:9,wire:[5,8,14],within:[13,14],work:0,wrapper:5,write:[],wsgiserver:13,x8hljhs9:13,x9su799iqakxujmvsbllq18my0f1cwior:[],x9su7lumqak:13,xn97zj7prn4adom88rxwwkumtrmfxi9crjb5s0rtnjoiwtjsrkmur3m:13,xu7wwwyqfub:13,y9xgay:[],yes:0,yield:6,ylecaqy2c5zorviuqlr:13,you:[0,2,5,8,9,13,14,15],your:[2,9,14,15],yubjhvequcxqe5:[],zero:[0,3,4,5],zk_get_seri:5,zk_get_str:5,zk_immediate_store_dis:5,zk_immediate_store_en:5,zone:[],zookeep:[3,4,5,6,8,12],zookeeper_group_id:3,zookeeperdatatoolargeexcept:[5,6],zookeepererror:5,zzr:13},titles:["eva.base.adapter","eva.base.executor","eva.config","eva","eva.eventloop","eva.eventqueue","eva.exceptions","API documentation","Configuration","Development","EVA: the Event Adapter","Introduction to Event Adapter","Metrics","HTTP REST API","Tutorial","Configuration directives"],titleterms:{"abstract":15,"class":15,"function":[],adapt:[0,14],adapter:[10,11],adding:14,adpter:[],all:0,anatomi:11,api:[7,13],automat:14,base:[0,1],check:13,client:13,code:14,config:2,configur:[0,8,14,15],contain:9,content:[],creat:14,develop:9,direct:15,docker:9,document:[7,9],environ:9,eva:[0,1,2,3,4,5,6,10,11],event:[10,11],eventloop:4,eventqueu:5,except:6,exception:[],execut:14,executor:1,file:8,format:8,gener:9,health:13,http:13,includ:15,indice:10,introduct:11,job:14,lint:9,load:14,metadata:14,metric:12,modul:[],onli:13,productstatu:14,read:13,report:[],request:13,rest:13,restart:14,rpc:13,run:9,section:15,set:9,shell:14,tabl:10,test:9,tutori:14,variabl:14,welcom:[],write:[13,14]}})