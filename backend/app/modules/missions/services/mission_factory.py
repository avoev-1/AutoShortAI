from app.modules.missions.domain.mission import CreationMode, Mission, MissionOptions

class MissionFactory:
    def create(self, title:str, platforms:list[str], creation_mode:CreationMode=CreationMode.assisted, target_duration_seconds:int=45, creation_profile:str="default") -> Mission:
        return Mission(title=title, options=MissionOptions(platforms=platforms, creation_mode=creation_mode, target_duration_seconds=target_duration_seconds, creation_profile=creation_profile))
