import json
from typing import Tuple, Any, Dict, Union

from janis_core.utils.logger import Logger


class Serializable:
    parse_types = {}

    def output(self):
        d = self.to_dict()
        tl = [(k + ": " + json.dumps(d[k], indent=2)) for k in d]
        return 'include required(classpath("application"))\n\n' + "\n".join(tl)

    @staticmethod
    def serialize(key, value) -> Tuple[str, Any]:
        if value is None:
            return key, None
        if isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
            return key, value
        elif isinstance(value, tuple):
            return Serializable.serialize(
                value[0], Serializable.serialize(None, value[1])[1]
            )
        elif isinstance(value, dict):
            return key, Serializable.serialize_dict(value)
        elif isinstance(value, list):
            return key, [Serializable.serialize(None, t)[1] for t in value]
        elif isinstance(value, Serializable):
            return key, value.to_dict()

        raise Exception(
            "Unable to serialize '{key}' of type '{value}".format(
                key=key, value=type(value)
            )
        )

    @staticmethod
    def serialize_dict(d):
        retval = {}
        for k, v in d.items():
            if v is None:
                continue
            k, v = Serializable.serialize(k, v)
            if not isinstance(v, bool) and not v:
                continue
            retval[k] = v
        return retval

    def to_dict(self):
        return self.serialize_dict(vars(self))

    @classmethod
    def from_dict(cls, d):
        import inspect

        kwargs = {}
        argspec = inspect.getfullargspec(cls.__init__)
        ptypes = cls.parse_types or {}

        for k in argspec.args:
            if k not in d:
                continue
            if k in ptypes:
                kwargs[k] = ptypes[k].from_dict(d[k])
            else:
                kwargs[k] = d[k]

        return cls.__init__(**kwargs)


class CromwellConfiguration(Serializable):
    """
    Based on information provided by: https://github.com/broadinstitute/cromwell/blob/develop/cromwell.examples.conf
    """

    JOBNAME_TRANSFORM = (
        '${sub(sub(cwd, ".*call-", ""), "/", "-")}-cpu-${cpu}-mem-${memory_mb}'
    )

    class Webservice(Serializable):
        def __init__(
            self, port=None, interface=None, binding_timeout=None, instance_name=None
        ):
            self.port = port
            self.interface = interface
            self.binding_timeout = ("binding-timeout", binding_timeout)
            self.instance_name = ("instance.name", instance_name)

    class Akka(Serializable):
        pass

    class System(Serializable):
        class Io(Serializable):
            def __init__(
                self, per=None, number_of_attempts=None, number_of_requests=None
            ):
                self.per = per
                self.number_of_attempts = ("number-of-attempts", number_of_attempts)
                self.number_of_requests = ("number-of-requests", number_of_requests)

        def __init__(
            self,
            io: Io = None,
            abort_jobs_on_terminate=None,
            graceful_server_shutdown=None,
            workflow_restart=None,
            max_concurrent_workflows=None,
            max_workflow_launch_count=None,
            new_workflow_poll_rate=None,
            number_of_workflow_log_copy_workers=None,
            number_of_cache_read_workers=None,
            job_shell=None,
            cromwell_id=None,
            cromwell_id_random_suffix=None,
        ):
            self.io = io
            self.abort_jobs_on_terminate = (
                "abort-jobs-on-terminate",
                abort_jobs_on_terminate,
            )
            self.graceful_server_shutdown = (
                "graceful-server-shutdown",
                graceful_server_shutdown,
            )
            self.workflow_restart = ("workflow-restart", workflow_restart)
            self.max_concurrent_workflows = (
                "max-concurrent-workflows",
                max_concurrent_workflows,
            )
            self.max_workflow_launch_count = (
                "max-workflow-launch-count",
                max_workflow_launch_count,
            )
            self.new_workflow_poll_rate = (
                "new-workflow-poll-rate",
                new_workflow_poll_rate,
            )
            self.number_of_workflow_log_copy_workers = (
                "number-of-workflow-log-copy-workers",
                number_of_workflow_log_copy_workers,
            )
            self.number_of_cache_read_workers = (
                "number-of-cache-read-workers",
                number_of_cache_read_workers,
            )
            self.job_shell = ("job-shell", job_shell)
            self.cromwell_id = cromwell_id
            self.cromwell_id_random_suffix = cromwell_id_random_suffix

    class Database(Serializable):
        class Db(Serializable):
            def __init__(self, driver, url, user, password, connection_timeout):
                self.driver = driver
                self.url = url
                self.user = user
                self.password = password
                self.connectionTimeout = connection_timeout

        def __init__(self, profile=None, insert_batch_size=None, db: Db = None):
            self.db = db
            self.profile = profile
            self.insert_batch_size = ("insert-batch-size", insert_batch_size)

        MYSQL_URL = "jdbc:mysql://{url}/{database}?rewriteBatchedStatements=true&useSSL=false&serverTimezone=UTC"

        @classmethod
        def mysql(
            cls,
            username=None,
            password=None,
            connection_timeout=5000,
            database="cromwell",
            url="localhost",
        ):
            return cls(
                profile="slick.jdbc.MySQLProfile$",
                db=cls.Db(
                    driver="com.mysql.cj.jdbc.Driver",
                    url=cls.MYSQL_URL.format(url=url, database=database),
                    user=username,
                    password=password,
                    connection_timeout=connection_timeout,
                ),
            )

    class Backend(Serializable):
        class Provider(Serializable):
            class Config(Serializable):
                def __init__(
                    self,
                    submit=None,
                    submit_docker=None,
                    runtime_attributes=None,
                    kill=None,
                    kill_docker=None,
                    check_alive=None,
                    job_id_regex=None,
                    concurrent_job_limit=None,
                    default_runtime_attributes=None,
                    filesystems=None,
                    run_in_background=None,
                    root=None,
                    **kwargs,
                ):
                    self.root = root
                    self.default_runtime_attributes = (
                        "default-runtime-attributes",
                        default_runtime_attributes,
                    )
                    self.concurrent_job_limit = (
                        "concurrent-job-limit",
                        concurrent_job_limit,
                    )
                    self.filesystems = filesystems
                    self.runtime_attributes = (
                        "runtime-attributes",
                        (runtime_attributes or "").replace("\n", "\\n"),
                    )

                    self.submit = submit
                    self.submit_docker = ("submit-docker", submit_docker)
                    self.kill = kill
                    self.kill_docker = ("kill-docker", kill_docker)
                    self.check_alive = ("check-alive", check_alive)
                    self.job_id_regex = ("job-id-regex", job_id_regex)
                    self.run_in_background = ("run-in-background", run_in_background)

                    for k, v in kwargs.items():
                        self.__setattr__(k, v)

            def __init__(
                self,
                actor_factory="cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory",
                config: Config = None,
            ):
                self.actor_factory = ("actor-factory", actor_factory)
                self.config = config

            @classmethod
            def slurm(cls):
                return cls(
                    actor_factory="cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory",
                    config=cls.Config(
                        runtime_attributes="""\
Int runtime_minutes = 1440
Int? cpu = 1
Int memory_mb = 3500
String? docker""".strip(),
                        submit="""
    jobname='${{sub(sub(cwd, ".*call-", ""), "/", "-")}}-cpu-${{cpu}}-mem-${{memory_mb}}'
    sbatch \\
        -J $jobname \\
        -D ${cwd} \\
        -o ${out} \\
        -e ${err} \\
        -t ${runtime_minutes} \\
        ${"-p " + queue} \\
        ${"-n " + cpu} \\
        --mem=${memory_mb} \\
        --wrap "/usr/bin/env ${job_shell} ${script}" """,
                        kill="scancel ${job_id}",
                        check_alive="scontrol show job ${job_id}",
                        job_id_regex="Submitted batch job (\\d+).*",
                    ),
                )

            @classmethod
            def slurm_singularity(
                cls,
                singularityloadinstructions,
                singularitycontainerdir,
                buildinstructions,
                jobemail,
                jobqueues,
                afternotokaycatch: bool = True,
                limit_resources: bool = False,
            ):
                slurm = cls.slurm()

                afternotokaycommand = ""
                if afternotokaycatch:
                    afternotokaycommand = " && NTOKDEP=$(sbatch --parsable --kill-on-invalid-dep=yes --dependency=afternotokay:$JOBID --wrap 'echo 1 >> ${cwd}/execution/rc')"

                partitions = (
                    ",".join(jobqueues) if isinstance(jobqueues, list) else jobqueues
                )
                partition_string = ("-p " + partitions) if partitions else ""
                emailextra = (
                    f"--mail-user {jobemail} --mail-type END" if jobemail else ""
                )

                cgroups_creation = (
                    """# Generate singularity cgroups command
                cgroupsfile="${cwd}/execution/singularity-cgroup.toml"
                printf "[memory]\\n  limit = $((${memory_mb} * 1048576))" > $cgroupsfile\
                """
                    if limit_resources
                    else ""
                )

                cgroups_binding = (
                    " --apply-cgroups $cgroupsfile" if limit_resources else ""
                )

                slurm.config.runtime_attributes = (
                    slurm.config.runtime_attributes[0],
                    """\
Int runtime_minutes = 1440
String kvruntime_value = ""
Int? cpu = 1
Int memory_mb = 3500
String? docker
""",
                )
                slurm.config.submit = None
                slurm.config.submit_docker = (
                    "submit-docker",
                    f"""
            {singularityloadinstructions}
            
            docker_subbed=$(sed -e 's/[^A-Za-z0-9._-]/_/g' <<< ${{docker}})
            image={singularitycontainerdir}/$docker_subbed.sif
            lock_path={singularitycontainerdir}/$docker_subbed.lock

            {cgroups_creation}
            
            if [ ! -f "$image" ]; then
              {buildinstructions}
            fi

            # Submit the script to SLURM
            jobname={CromwellConfiguration.JOBNAME_TRANSFORM}
            JOBID=$(sbatch \\
                --parsable \\
                -J $jobname \\
                --mem=${{memory_mb}} \\
                --cpus-per-task ${{if defined(cpu) then cpu else 1}} \\
                {partition_string} \\
                -D ${{cwd}} \\
                -o ${{cwd}}/execution/stdout \\
                -e ${{cwd}}/execution/stderr \\
                -t ${{runtime_minutes}} \\
                {emailextra} \\
                --wrap "singularity exec --bind ${{cwd}}:${{docker_cwd}}{cgroups_binding} $image ${{job_shell}} ${{docker_script}}") \\
                {afternotokaycommand} \\
                && echo Submitted batch job $JOBID
            """,
                )
                return slurm

            @classmethod
            def singularity(
                cls,
                singularityloadinstructions,
                singularitycontainerdir,
                buildinstructions,
                limit_resources: bool = False,
                executionDirectory: str = None,
            ):

                config = cls(
                    actor_factory="cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory",
                    config=cls.Config(
                        runtime_attributes="""\
String? docker""".strip(),
                        run_in_background=True,
                        root=executionDirectory,
                    ),
                )

                cgroups_creation = (
                    """# Generate singularity cgroups command
                cgroupsfile="${{cwd}}/execution/singularity-cgroup.toml"
                printf "[memory]\\n  limit = $((${{memory_mb}} * 1048576))" > $cgroupsfile\
                """
                    if limit_resources
                    else ""
                )
                cgroups_binding = (
                    " --apply-cgroups $cgroupsfile" if limit_resources else ""
                )

                config.config.submit_docker = (
                    "submit-docker",
                    f"""
                    {singularityloadinstructions}

                    docker_subbed=$(sed -e 's/[^A-Za-z0-9._-]/_/g' <<< ${{docker}})
                    image={singularitycontainerdir}/$docker_subbed.sif
                    lock_path={singularitycontainerdir}/$docker_subbed.lock

                    if [ ! -f "$image" ]; then
                      (
                      flock --exclusive 200 1>&2
                      if [ ! -f "$image" ]; then
                        {buildinstructions}
                      fi
                      ) 200>$lock_path
                    fi

                    {cgroups_creation}

                    singularity exec --bind ${{cwd}}:${{docker_cwd}}{cgroups_binding} $image ${{job_shell}} ${{docker_script}}
                    """,
                )
                return config

            # noinspection PyPep8
            @classmethod
            def torque(cls, queue):
                """
                Source: https://gatkforums.broadinstitute.org/wdl/discussion/12992/failed-to-evaluate-job-outputs-error
                """
                return cls(
                    actor_factory="cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory",
                    config=cls.Config(
                        runtime_attributes=f"""
    String queue = "{queue}"
    Int runtime_minutes = 1439
    Int? cpu = 1
    Int memory_mb = 3500
     """,
                        submit="""
    chmod +x ${script}
    echo "${job_shell} ${script}" | qsub -V -d ${cwd} -N ${job_name} -o ${out} -e ${err} -q ${queue} -l nodes=1:ppn=${cpu}" \
        -l walltime=${walltime} -l mem=${memory_mb}
            """,
                        job_id_regex="^(\\d+).*",
                        kill="qdel ${job_id}",
                        check_alive="qstat ${job_id}",
                    ),
                )

            @classmethod
            def torque_singularity(
                cls,
                queue,
                singularityloadinstructions,
                singularitycontainerdir,
                buildinstructions,
                send_job_updates,
                afternotokaycatch=False,
            ):
                """
                Source: https://gatkforums.broadinstitute.org/wdl/discussion/12992/failed-to-evaluate-job-outputs-error
                """

                from janis_assistant.management.configuration import JanisConfiguration

                torq = cls.torque(queue)

                afternotokaycommand = ""
                if afternotokaycatch:
                    afternotokaycommand = " && NTOKDEP=$(echo 'echo 1 >> ${cwd}/execution/rc' | qsub depend=afternotok:$JOBID)"

                emailparams = ""
                email = JanisConfiguration.manager().notifications.email
                if send_job_updates:
                    if not email:
                        Logger.info(
                            "Skipping send_job_updates for Torque as no email was found in the configuration"
                        )
                    else:
                        emailparams = f"-m ea -M {email}"

                loadinstructions = (
                    (singularityloadinstructions + " &&")
                    if singularityloadinstructions
                    else ""
                )

                torq.config.kill_docker = (torq.config.kill_docker[0], torq.config.kill)

                torq.config.submit = None
                torq.config.runtime_attributes = (
                    torq.config.runtime_attributes[0],
                    """\
    Int runtime_minutes = 1440
    Int? cpu = 1
    Int memory_mb = 3500
    String? docker""",
                )

                torq.config.submit_docker = (
                    "submit-docker",
                    f"""
    docker_subbed=$(sed -e 's/[^A-Za-z0-9._-]/_/g' <<< ${{docker}})
    image={singularitycontainerdir}/$docker_subbed.sif
    jobname={CromwellConfiguration.JOBNAME_TRANSFORM}
    walltime='23:00:00' # $(echo $((${{runtime_minutes}} * 60)) | dc -e '?1~r60~r60~r[[0]P]szn[:]ndZ2>zn[:]ndZ2>zn')

    if [ ! -f $image ]; then
        {singularityloadinstructions}
        {buildinstructions}
    fi
    
    echo \
        "{loadinstructions} \\
        singularity exec --bind ${{cwd}}:${{docker_cwd}} $image ${{job_shell}} ${{script}}" |\\
        JOBID=$(qsub \\
            -v ${{cwd}} \\
            -N $jobname \\
            {emailparams} \\
            -o ${{cwd}}/execution/stdout \\
            -e ${{cwd}}/execution/stderr \\
            -l nodes=1:ppn=${{cpu}},mem=${{memory_mb}}mb,walltime=$walltime  | awk 'match($0,/[0-9]+/){{print substr($0, RSTART, RLENGTH)}}')  \\
        {afternotokaycommand} \\
        && echo $JOBID
    """,
                )
                return torq

            @classmethod
            def aws(cls, s3_bucket, queue_arn):
                return cls(
                    actor_factory="cromwell.backend.impl.aws.AwsBatchBackendLifecycleActorFactory",
                    config=cls.Config(
                        root="s3://{bucket}/cromwell-execution".format(
                            bucket=s3_bucket
                        ),
                        numSubmitAttempts=3,
                        numCreateDefinitionAttempts=3,
                        auth="default",
                        concurrent_job_limit=16,
                        default_runtime_attributes={"queueArn": queue_arn},
                        filesystems={"s3": {"auth": "default"}},
                    ),
                )

        def __init__(self, default="Local", providers=Dict[str, Provider]):

            self.default = default
            self.providers = providers

            if default not in providers:
                if len(providers) == 1:
                    backend_key = next(iter(providers.keys()))
                    Logger.warn(
                        "The default tag '{default}' was not found in the providers, this was automatically "
                        "corrected to be '{backend_key}'.".format(
                            default=default, backend_key=backend_key
                        )
                    )
                    self.default = default
                else:
                    raise Exception(
                        "The default tag '{default}' was not found in the providers and couldn't be "
                        "automatically corrected".format(default=default)
                    )

        @staticmethod
        def with_new_local_exec_dir(execution_directory: str):
            return CromwellConfiguration.Backend(
                providers={
                    "Local": CromwellConfiguration.Backend.Provider(
                        config=CromwellConfiguration.Backend.Provider.Config(
                            root=execution_directory
                        )
                    )
                }
            )

    class Engine(Serializable):
        def __init__(self, s3: Union[bool, str] = None, gcs: Union[bool, str] = None):
            self.filesystems = {}

            if s3:
                self.filesystems["s3"] = self._s3(s3)
            if gcs:
                self.filesystems["gcs"] = self._gcs(gcs)

        @staticmethod
        def _gcs(obj):
            if isinstance(obj, bool):
                return {"auth": "application-default"}
            return obj

        @staticmethod
        def _s3(obj):
            if isinstance(obj, bool):
                return {"auth": "default"}
            return obj

    class AWS(Serializable):
        class Auth(Serializable):
            def __init__(
                self, name="default", scheme="default", access_key=None, secret_key=None
            ):
                self.name = name
                self.scheme = scheme

                self.access_key = ("access-key", access_key)
                self.secret_key = ("secret-key", secret_key)

        def __init__(self, region, application_name="cromwell", auths=None):
            self.region = region
            self.application_name = ("application-name", application_name)
            if auths is None:
                auths = [self.Auth()]
            self.auths = auths if isinstance(auths, list) else [auths]

    class Docker(Serializable):
        class HashLookup(Serializable):
            def __init__(self, enabled=True):
                self.enabled = enabled

        def __init__(self, hash_lookup=None):
            if hash_lookup is not None and not isinstance(hash_lookup, self.HashLookup):
                raise Exception(
                    "hash-lookup is not of type CromwellConfiguration.Docker.HashLookup"
                )
            self.hash_lookup = ("hash-lookup", hash_lookup)

    class CallCaching(Serializable):
        class BlacklistCache(Serializable):
            def __init__(self, enabled=None, concurrency=None, ttl=None, size=None):
                self.enabled = enabled
                self.concurrency = concurrency
                self.ttl = ttl
                self.size = size

        def __init__(
            self, enabled=True, invalidate_bad_cache_results=None, blacklist_cache=None
        ):
            if blacklist_cache is not None and not isinstance(
                blacklist_cache, self.BlacklistCache
            ):
                raise Exception(
                    "hash-lookup is not of type CromwellConfiguration.Docker.HashLookup"
                )
            self.enabled = enabled
            self.invalidate_bad_cache_results = (
                "invalidate-bad-cache-results",
                invalidate_bad_cache_results,
            )
            self.hash_lookup = ("blacklist-cache", blacklist_cache)

    def __init__(
        self,
        webservice: Webservice = None,
        akka: Akka = None,
        system: System = None,
        database: Database = None,
        backend: Backend = None,
        engine: Engine = None,
        docker: Docker = None,
        cache: CallCaching = None,
        aws=None,
    ):
        if webservice is not None and isinstance(
            webservice, CromwellConfiguration.Webservice
        ):
            raise Exception("webservice not of type CromwellConfiguration.Webservice")
        self.webservice = webservice
        if akka is not None and not isinstance(akka, CromwellConfiguration.Akka):
            raise Exception("akka not of type CromwellConfiguration.Akka")
        self.akka = akka
        if system is not None and not isinstance(system, CromwellConfiguration.System):
            raise Exception("system not of type CromwellConfiguration.System")
        self.system = system
        if database is not None and not isinstance(
            database, CromwellConfiguration.Database
        ):
            raise Exception("database not of type CromwellConfiguration.Database")
        self.database = database
        if backend is not None and not isinstance(
            backend, CromwellConfiguration.Backend
        ):
            raise Exception("backend not of type CromwellConfiguration.Backend")
        self.backend = backend
        if engine is not None and not isinstance(engine, CromwellConfiguration.Engine):
            raise Exception("engine not of type CromwellConfiguration.Engine")
        self.engine = engine
        if docker is not None and not isinstance(docker, CromwellConfiguration.Docker):
            raise Exception("docker not of type CromwellConfiguration.Docker")
        self.docker = docker
        if cache is not None and not isinstance(
            cache, CromwellConfiguration.CallCaching
        ):
            raise Exception("cache not of type CromwellConfiguration.CallCaching")
        self.call_caching = ("call-caching", cache)

        if aws is not None and not isinstance(aws, CromwellConfiguration.AWS):
            raise Exception("aws not of type CromwellConfiguration.AWS")
        self.aws = aws


if __name__ == "__main__":
    # config = CromwellConfiguration.udocker_slurm()
    # config = CromwellConfiguration.udocker_torque()
    config = CromwellConfiguration(
        aws=CromwellConfiguration.AWS(
            region="ap-southeast-2", auths=[CromwellConfiguration.AWS.Auth()]
        ),
        engine=CromwellConfiguration.Engine(s3=True)
        # backend=CromwellConfiguration.Backend(
        #     default="singularity",
        #     providers={"singularity": CromwellConfiguration.Backend.Provider.slurm_singularity()}
        # ),
    )
    print(config.output())
    # open("configuration.conf", "w+").write(config)

_aws = """
include required(classpath("application"))

aws {
  application-name = "cromwell"
  auths = [{
      name = "default"
      scheme = "default"
  }]
  region = "ap-southeast-2"
}

engine { filesystems { s3 { auth = "default" } } }

backend {
  default = "AWSBATCH"
  providers {
    AWSBATCH {
      actor-factory = "cromwell.backend.impl.aws.AwsBatchBackendLifecycleActorFactory"
      config {
        numSubmitAttempts = 3
        numCreateDefinitionAttempts = 3
        root = "s3://cromwell-logs/cromwell-execution"
        auth = "default"
        concurrent-job-limit = 16
        default-runtime-attributes {
          queueArn = "arn:aws:batch:ap-southeast-2:518581388556:compute-environment/GenomicsDefaultComputeE-2c00719e0b6be8f"
        }
        filesystems { s3 { auth = "default" } }
      }
    }
  }
}
"""

_slurm = """
include required(classpath("application"))

backend {
  providers {
    default: SLURM
    SLURM {
      actor-factory = "cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory"
      config {
        runtime-attributes = \"""
        Int runtime_minutes = 600
        Int cpu = 2
        Int requested_memory_mb_per_core = 8000
        String queue = "short"
        ""\"
        
        submit = \"""
            sbatch -J ${job_name} -D ${cwd} -o ${out} -e ${err} -t ${runtime_minutes} -p ${queue} \
            ${"-c " + cpu} \
            --mem-per-cpu=${requested_memory_mb_per_core} \
            --wrap "/bin/bash ${script}"
        ""\"
        kill = "scancel ${job_id}"
        check-alive = "scontrol show job ${job_id}"
        job-id-regex = "Submitted batch job (\\d+).*"
      }
    }
  }
}
"""

_mysql = """
include required(classpath("application"))

database {
  profile = "slick.jdbc.MySQLProfile$"
  db {
    driver = "com.mysql.jdbc.Driver"
    url = "jdbc:mysql://localhost/cromwell?useSSL=false&rewriteBatchedStatements=true"
    user = "user"
    password = "pass"
    connectionTimeout = 5000
  }
  metadata {
    profile = "slick.jdbc.HsqldbProfile$"
    db {
      driver = "org.hsqldb.jdbcDriver"
      url = "jdbc:hsqldb:file:metadata/;shutdown=false;hsqldb.tx=mvcc"
      connectionTimeout = 3000
    }
  }
}
"""

_udocker = """
include required(classpath("application"))

docker.hash-lookup.enabled = false

backend {
    default: udocker
    providers: {
        udocker {
            # The backend custom configuration.
            actor-factory = "cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory"

            config {
                run-in-background = true
                # The list of possible runtime custom attributes.
                runtime-attributes = \"""
                String? docker
                String? docker_user
                ""\"

                # Submit string when there is a "docker" runtime attribute.
                submit-docker = \"""
                udocker run \
                  ${"--user " + docker_user} \
                  -v ${cwd}:${docker_cwd} \
                  ${docker} ${job_shell} ${script}
                ""\"
            }
        }
    }
}
"""
