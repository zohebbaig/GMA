import os

def populate():
    intro = "This is a dummy introduction for users: Greater was make of thing called living green cattle bring was air bring years given beast herb created meat the multiply gathering moving sixth divide there. Dominion whose itself. Multiply abundantly moved."
    desc = "This is a dummy description of groups: Groups within the GMA system"

    # Create users
    u_zoheb = add_user("zoheb", "Zoheb", "Baig", "zohebb@email.com", intro)
    u_john = add_user("john", "John", "Smith", "johns@email.com", intro)
    u_bobby = add_user("bobby", "Bobby", "Taylor", "bobbyt@email.com", intro)
    u_chris = add_user("chris", "Chris", "Kerr", "chrisk@email.com", intro)
    u_david = add_user("david", "David", "Thomas", "davidt@email.com", intro)
    u_helen = add_user("helen", "Helen", "Potters", "helenp@email.com", intro)
    u_frank = add_user("frank", "Frank", "Carter", "frankc@email.com", intro)
    u_adam = add_user("adam", "Adam", "Bell", "adamb@email.com", intro)
    u_edward = add_user("edward", "Edward", "Foley", "edwardf@email.com", intro)
    u_graham = add_user("graham", "Graham", "Davidson", "grahamd@email.com", intro)
    u_kerry = add_user("kerry", "Kerry", "Laidlaw", "kerryl@email.com", intro)
    u_liam = add_user("liam", "Liam", "Tisk", "liamt@email.com", intro)
    u_mark = add_user("mark", "Mark", "Myers", "markm@email.com", intro)
    u_norman = add_user("norman", "Norman", "Cook", "normanc@email.com", intro)
    u_oliver = add_user("oliver", "Oliver", "Reid", "oliverr@email.com", intro)
    u_peter = add_user("peter", "Peter", "Parker", "peterp@email.com", intro)
    u_rona = add_user("rona", "Rona", "Weir", "ronaw@email.com", intro)
    u_sarah = add_user("sarah", "Sarah", "Bain", "sarahb@email.com", intro)
    u_tina = add_user("tina", "Tina", "Malone", "tinam@email.com", intro)
    u_uma = add_user("uma", "Uma", "Thurman", "umat@email.com", intro)
    u_victoria = add_user("victoria", "Victoria", "Jones", "victoriaj@email.com", intro)
    u_william = add_user("william", "William", "Paterson", "williamp@email.com", intro)
    u_yolanda = add_user("yolanda", "Yolanda", "Mugdock", "yolandam@email.com", intro)
    u_ian = add_user("ian", "Ian", "Mitchell", "ianm@email.com", intro)
    u_quinn = add_user("quinn", "Quinn", "Foster", "quinnf@email.com", intro)
    u_xena = add_user("xena", "Xena", "Peterson", "xenap@email.com", intro)



    # Create groups
    g_prog = add_group("Programming", desc, u_zoheb)
    g_sn = add_group("Systems and Networks", desc, u_zoheb)
    g_proj = add_group("Project", desc, u_bobby)
    g_se = add_group("Software Engineering", desc, u_bobby)
    g_re = add_group("Requirements Engineering", desc, u_john)
    g_ec = add_group("Enterprise Computing", desc, u_chris)
    g_cs = add_group("Cyber Security", desc, u_john)
    g_it = add_group("Internet Technology", desc, u_chris)
    g_spn = add_group("Software Project Management", desc, u_david)
    g_tis = add_group("Trends Information Security", desc, u_david)
    g_hci = add_group("Human Computer Interaction", desc, u_helen)
    g_ads = add_group("Algorithms Data Structures", desc, u_helen)
    g_advp = add_group("Advanced Programming", desc, u_frank)
    g_dt = add_group("Data Retrieval", desc, u_frank)
    g_ai = add_group("Artificial Intelligence", desc, u_adam)
    g_psi = add_group("Professional Skills Issues", desc, u_helen)
    g_pyt = add_group("Python Programming", desc, u_edward)
    g_dja = add_group("Django Programming", desc, u_graham)
    g_jav = add_group("Java Programming", desc, u_kerry)
    g_csc = add_group("Cost Saving Committee", desc, u_liam)
    g_its = add_group("Information Technology Support", desc, u_mark)



    # Add user to group's member list
    add_user_to_group(user=u_zoheb, group=g_prog)
    add_user_to_group(user=u_zoheb, group=g_sn)
    add_user_to_group(user=u_john, group=g_prog)
    add_user_to_group(user=u_bobby, group=g_proj)
    add_user_to_group(user=u_chris, group=g_se)
    add_user_to_group(user=u_xena, group=g_re)
    add_user_to_group(user=u_quinn, group=g_ec)
    add_user_to_group(user=u_zoheb, group=g_cs)
    add_user_to_group(user=u_ian, group=g_it)
    add_user_to_group(user=u_yolanda, group=g_spn)
    add_user_to_group(user=u_william, group=g_tis)
    add_user_to_group(user=u_victoria, group=g_hci)
    add_user_to_group(user=u_uma, group=g_ads)
    add_user_to_group(user=u_zoheb, group=g_advp)
    add_user_to_group(user=u_zoheb, group=g_proj)
    add_user_to_group(user=u_tina, group=g_dt)
    add_user_to_group(user=u_sarah, group=g_ai)
    add_user_to_group(user=u_rona, group=g_psi)
    add_user_to_group(user=u_chris, group=g_prog)
    add_user_to_group(user=u_peter, group=g_pyt)
    add_user_to_group(user=u_oliver, group=g_dja)
    add_user_to_group(user=u_norman, group=g_jav)
    add_user_to_group(user=u_chris, group=g_csc)
    add_user_to_group(user=u_chris, group=g_its)
    add_user_to_group(user=u_john, group=g_sn)
    add_user_to_group(user=u_john, group=g_proj)
    add_user_to_group(user=u_john, group=g_se)
    add_user_to_group(user=u_david, group=g_prog)
    add_user_to_group(user=u_david, group=g_proj)
    add_user_to_group(user=u_david, group=g_sn)
    add_user_to_group(user=u_helen, group=g_its)
    add_user_to_group(user=u_zoheb, group=g_its)
    add_user_to_group(user=u_zoheb, group=g_csc)
    add_user_to_group(user=u_david, group=g_proj)
    add_user_to_group(user=u_william, group=g_cs)
    add_user_to_group(user=u_frank, group=g_ec)
    add_user_to_group(user=u_frank, group=g_re)
    add_user_to_group(user=u_xena, group=g_it)
    add_user_to_group(user=u_quinn, group=g_spn)
    add_user_to_group(user=u_yolanda, group=g_tis)
    add_user_to_group(user=u_uma, group=g_hci)
    add_user_to_group(user=u_tina, group=g_ads)
    add_user_to_group(user=u_victoria, group=g_advp)
    add_user_to_group(user=u_victoria, group=g_proj)
    add_user_to_group(user=u_rona, group=g_dt)
    add_user_to_group(user=u_sarah, group=g_psi)
    add_user_to_group(user=u_graham, group=g_psi)
    add_user_to_group(user=u_adam, group=g_advp)
    add_user_to_group(user=u_edward, group=g_psi)
    add_user_to_group(user=u_kerry, group=g_psi)
    add_user_to_group(user=u_liam, group=g_psi)
    add_user_to_group(user=u_mark, group=g_psi)
    add_user_to_group(user=u_sarah, group=g_spn)
    add_user_to_group(user=u_zoheb, group=g_psi)



    # Add user to another user's contact list.
    add_contact(user=u_zoheb, contact=u_bobby)
    add_contact(user=u_bobby, contact=u_zoheb)
    add_contact(user=u_john, contact=u_chris)
    add_contact(user=u_chris, contact=u_john)
    add_contact(user=u_zoheb, contact=u_adam)
    add_contact(user=u_adam, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_david)
    add_contact(user=u_david, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_edward)
    add_contact(user=u_edward, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_frank)
    add_contact(user=u_frank, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_graham)
    add_contact(user=u_graham, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_helen)
    add_contact(user=u_helen, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_ian)
    add_contact(user=u_ian, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_john)
    add_contact(user=u_john, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_kerry)
    add_contact(user=u_kerry, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_liam)
    add_contact(user=u_liam, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_mark)
    add_contact(user=u_mark, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_norman)
    add_contact(user=u_norman, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_oliver)
    add_contact(user=u_oliver, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_peter)
    add_contact(user=u_peter, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_quinn)
    add_contact(user=u_quinn, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_rona)
    add_contact(user=u_rona, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_sarah)
    add_contact(user=u_sarah, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_tina)
    add_contact(user=u_tina, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_uma)
    add_contact(user=u_uma, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_victoria)
    add_contact(user=u_victoria, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_william)
    add_contact(user=u_william, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_xena)
    add_contact(user=u_xena, contact=u_zoheb)
    add_contact(user=u_zoheb, contact=u_yolanda)
    add_contact(user=u_yolanda, contact=u_zoheb)



    # Send message from recipient to sender, timestamp is added automatically by the DB
    send_message(text="Hello", recipient=u_bobby, sender=u_zoheb)
    send_message(text="How are you?", recipient=u_zoheb, sender=u_bobby)
    send_message(text="Good thanks, meet for lunch?", recipient=u_bobby, sender=u_zoheb)
    send_message(text="Sure, see you at 12pm?", recipient=u_zoheb, sender=u_bobby)


def add_user(username, fname, lname, email, introduction):
    p = User.objects.get_or_create(username=username, first_name=fname, last_name=lname, email=email)[0]
    p.set_password("password")
    UserProfile.objects.get_or_create(user=p, introduction=introduction)
    p.save()
    return p


def add_group(name, desc, owner):
    g = Group.objects.get_or_create(name=name, description=desc, owner=owner)[0]
    add_user_to_group(owner, g)
    return g


def add_user_to_group(user, group):
    group.members.add(user)


def add_contact(user, contact):
    profile = user.profile
    profile.contacts.add(contact)
    profile.save()


def send_message(sender, recipient, text):
    msg = Message(text=text, sender=sender, recipient=recipient.profile)
    msg.save()


if __name__ == '__main__':
    print "Populating the database"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging.settings')
    from messaging.models import UserProfile, Group, Message
    from django.contrib.auth.models import User

    populate()
    print "DONE"