use std::{process::Command, fs::File, env::current_dir, io::Read};
use json;


fn do_update() {
    // TODO
}


fn check_update() -> bool {

    Command::new("curl")
    .arg("-o")
    .arg("tags.json")
    .arg("https://api.github.com/repos/mohsarmad/Clocou/tags")
    .spawn()
    .and_then(|_| {
        let cur_dir = current_dir().unwrap();

        let tags_json_path = cur_dir.join("tags.json");

        let mut tags_json_file = File::open(tags_json_path).unwrap();

        let mut buffer = String::new();
        Read::read_to_string(&mut tags_json_file, &mut buffer).unwrap();

        let tags_json = json::parse(&buffer).unwrap();

        let mut tags = Vec::new();

        for item in tags_json.members() {
            let last_tag = item["name"].as_str().unwrap();
            tags.push(last_tag);
        }

        let mut buffer = String::new();
        let mut conf_file = File::open(cur_dir.join("clocou.conf")).unwrap();
        conf_file.read_to_string(&mut buffer).unwrap();

        if buffer != tags[0] {
            return Ok(true);
        }

        Ok(false)
    })
    .expect("Running curl command failed!")
    
}


fn main() {
    
    let needs_updating = check_update();
    if needs_updating {
        do_update();
        return;
    }

    println!("All is up to date!");

    // TODO: run the main application
}
