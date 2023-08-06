"""
MIT License

Copyright (c) 2019 Shortty10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def parse_report(url):
    """
    Parse the report's HTML into a Report object.

    Parameters
    -------------
    url: :class:`str`
        The report URL

    Raises
    -------------
    ValueError
        Parsing failed (Invalid ID / Glitched report)

    Returns
    -------------
    :class:`Report`
        The Report object.
    """
    request = requests.get(url).text
    if request in ["Could not find any reports with that ID.", "No report file found."]:
        raise ValueError("Report not found.")
    soup = BeautifulSoup(request, "lxml")

    data = {}

    judgement = soup.find("div", id="splash")
    if not judgement:
        judgement = "Open"
    elif judgement.text == "This report has been closed without judgement.":
        judgement = "Closed"
    elif judgement.text == "This report has been deemed guilty.":
        judgement = "Guilty"
    elif judgement.text == "This report has been deemed innocent.":
        judgement = "Innocent"

    data['judgement'] = judgement

    data['id'] = soup.find("span", class_="reportId").text

    data['user'] = soup.find("span", class_="reportedPlayer").text

    data['reason'] = soup.find("span", class_="reportReason").text

    data['ranked'] = bool("Ranked Game." in soup.find(
        "span", class_="notice").text)

    data['players'] = str(soup.find_all("script")).split(
        'data =')[1].split("}]};")[0] + "}]}"

    data['content'] = list(
        soup.find("div", id="reportContent").find_all("span"))

    data['date'] = soup.find("span", class_="reportDate").text

    data['details'] = str(soup.find("span", class_='reportDescription')).split(
        '<span class="reportDescription">')[1].split('</span>')[0].split("<br/>")

    data['details'] = [] if data['details'] == [''] else data['details']

    # Unescape HTML
    data['details'] = [msg.replace("&gt;", ">").replace(
        "&amp;", "&") for msg in data['details']]

    try:
        return Report(data)
    except Exception:
        raise ValueError("There was an error processing this report.")


def _get_player(name, players):
    data = {}
    data['all_players'] = players
    players = json.loads(players)["players"]

    # Fix bugged usernames
    if "(" in name:
        name = name.split("(")[0]

    # Check if 'name' is a username
    if name in [x["username"] for x in players]:
        data['name'] = name
        data['type'] = "username"
        return Player(data)

    # Check if 'name' is an IGN
    if name in [x["ign"] for x in players]:
        data['name'] = name
        data['type'] = "ign"
        return Player(data)

    # Otherwise, the report is bugged.
    # This is extremely rare (occurs in about 0.3% of reports).
    # Returns None to avoid an error.
    return None


class Report:
    """
    Represents a report parsed through parse_report(url).

    Attributes
    -------------
    id: :class:`int`
        The report ID.
    reported: :class:`Player`
        The reported player.
    reason: :class:`str`
        The reason for the report. e.g Gamethrowing, Cheating, Spamming.
    details: [:class:`str`]
        Reasons given by the reporters.
    is_ranked: :class:`bool`
        Returns True if the report is for a ranked game, otherwise False.
    judgement: :class:`str`
        The report's judgement. e.g Guilty, Innocent, Open, Closed.
    content: [:class:`Event`]
        The report's events. e.g messages, deaths, trials etc.
    dt: :class:`int`
        The time in seconds between the epoch and the time the report was submitted.
    players: [:class:`Player`]
        The players who took part in the game.
    winner: :class:`str`
        The faction that won the game. e.g "Mafia", "Town".
        Can also return "Stalemate" or "Draw".
        Can sometimes return None for reports submitted before December 2017.
    """

    def __init__(self, data):

        self.winner = None

        self.players = []

        players = data['players']

        plys = json.loads(players)['players']
        for player in plys:
            retry = False
            try:
                self.players.append(_get_player(player['username'], players))
                if not self.players[-1]:
                    self.players.pop()
                    retry = True
            except KeyError:
                retry = True
            if retry:
                try:
                    self.players.append(_get_player(player['ign'], players))
                except KeyError:
                    self.players.append(None)

        reported = _get_player(data['user'], players)

        content = data['content']

        # Convert date to POSIX timestamp
        date = data['date']
        if date[-8:-7] == " ":
            date = date[:14] + "0" + date[14:]
        date = int(datetime.strptime(
            date, "%b. %d, %Y %I:%M %p").timestamp())

        game_over = False

        # Convert elements from Soup to string
        content = [str(message) for message in content]

        # Remove all messages before day 1
        content = content[content.index(
            '<span class="time day">Day 1</span>'):]

        for message in content[::]:
            # Remove wills and death notes
            if '<span class="note"' in message:
                content.remove(message)

            # Remove messages from dead people
            elif 'dead">' in message or 'dead" title="' in message:
                content.remove(message)

            # Remove "has died" messages. We will instead use "was attacked by" messages to find deaths.
            elif '<span class="notice' in message and 'death"' in message:
                if not ' has been lynched.</span>' in message:
                    content.remove(message)

            # Remove "End of Report" messages.
            elif '<span class="end">End of Report</span>' in message:
                content.remove(message)

            # Remove "vampires have bitten" messages. We will instead use "was converted to" messages to find vampire bites.
            elif '<span class="Vampire vampire" title="">*Vampires have bit ' in message:
                content.remove(message)

            # Remove "has forged the will" notices
            elif '<span class="notice"' in message and ' has forged the will.</span>' in message:
                content.remove(message)

            # Remove glitched messages
            elif '<span class="" title=""></span>' in message or '<span class="seance" title=""></span>' in message:
                content.remove(message)
            else:
                try:
                    class_ = message.split(
                        '<span class="')[1].split('" title="">')[0].replace(" ", "")
                    txt = message.split('" title="">')[
                        1].split("</span>")[0].replace(" ", "")
                    if not class_ in ['notice', 'time day', 'time night', 'stage'] and class_ in txt:
                        content.remove(message)
                        continue
                except (IndexError, ValueError):
                    pass
                if '<span class="notice' in message and 'Witch control"' in message:
                    if not 'made' in message or not 'target' in message:
                        content.remove(message)

        new_list = []

        for message in content:
            if '<span class="stage">GameOver</span>' in message:
                game_over = True
                continue

            if 'class="notice"' in message:
                # Find if the message contains the winner
                if "has won.</span>" in message:
                    winner = message.split('">')[
                        1].split(" has won.</span>")[0]
                    self.winner = winner
                    break
                if '">Stalemate.</span>' in message:
                    self.winner = "Stalemate"
                    break
                if '>Draw.</span>' in message:
                    self.winner = "Draw"
                    break

                # Break at the end of the report
                if game_over:
                    self.winner = None
                    break
            elif game_over or '<span class="end">End of Report</span>' in message:
                self.winner = None
                break

            event_data = {}
            event_data['msg'] = message
            event_data['players'] = players
            new_list.append(Event(event_data))

        data['content'] = new_list

        self.reported = reported
        self.id = int(data["id"])
        self.reason = data["reason"]
        self.details = data["details"]
        self.is_ranked = data['ranked']
        self.judgement = data['judgement']
        self.content = data['content']
        self.dt = data['date']

    def __repr__(self):
        return str(self.id)


class Event:
    """
    Represents an event that occured (messages, deaths, etc.).

    Attributes
    -------------
    day: :class:`int`
        The day that has begun.
        Returns None if the event was not a new day.
    night: :class:`int`
        The night that has begun.
        Returns None if the event was not a new night.
    message: :class:`str`
        The message sent.
        Returns None if the event was not a message or whisper.
    is_jail: :class:`bool`
        Returns True if the message was sent in jail, otherwise False.
        Returns None if the event was not a message.
    is_mafia: :class:`bool`
        Returns True if the message was sent in mafia chat, otherwise False.
        Returns None if the event was not a message.
    author: :class:`Player`
        The player who sent the message/whisper.
        Returns None if the event was not a message or whisper.
    type: :class:`str`
        The type of event, e.g "Message", "Death", "Investigation", "Sheriff" etc.
    killed: :class:`Player`
        The player who was killed.
        Returns None if the event was not a death.
    killer: :class:`str`
        The role/faction that killed the player. e.g "Mafia", "Veteran", "Jailor"
        Returns "Guilt" when a vigilante shoots themselves.
        Returns "Guarding" when a bodyguard dies protecting someone.
        Returns "Lynch" if the player was lynched.
        Returns "Heartbreak" if the player died from heartbreak.
        Returns None if the event was not a death.
    visitor: :class:`Player`
        The player who visited.
        Can also be a string representing the visitor's faction, e.g vampire bites will return "Vampire"
        Returns None if the event was not an ability.
    visited: :class:`Player`
        The player who was visited.
        Returns None if no player was visited.
    recipient: :class:`Player`
        The player who the whisper was sent to.
        Returns None if the event was not a whisper.
    leaver: :class:`Player`
        The player who left the game.
        Returns None if the event was not a player leaving the game.
    voter: :class:`Player`
        The player who submitted the vote.
        Returns None if the event was not a vote.
    verdict: :class:`str`
        The verdict of the voter. (Abstain, Guilty, Innocent)
        Returns None if the event was not a vote.
    revived: :class:`Player`
        The player who was revived.
        Returns None if the event was not a revive.
    witched: :class:`Player`
        The player who was witched.
        Returns None if the event was not a witch.
    witch_target: :class:`Player`
        The target who the player was witched into.
        Returns None if the event was not a witch.
    witcher: :class:`str`
        The role that witched the player. Always returns "Witch", "CovenLeader" or "Necromancer"
        Returns None if the event was not a witch.
    amne: :class:`Player`
        The amnesiac who remembered they were like a role.
        Returns None if the event was not a remember.
    remembered: :class:`str`
        The role that the amnesiac remembered they were like.
        Returns None if the event was not a remember.
    converted: :class:`Player`
        The player who was converted to the vampires.
        Returns None if the event was not a conversion.
    transported: [:class:`Player]
        The two players who were transported.
        Returns None if the event was not a transport.
    revealer: :class:`Player`
        The mayor who revealed.
        Returns None if the event was not a reveal.
    """

    def __init__(self, data):
        message = data['msg']
        all_players = data['players']
        self.day = None
        self.night = None
        self.message = None
        self.is_jail = None
        self.is_mafia = None
        self.author = None
        self.type = None
        self.killed = None
        self.killer = None
        self.visitor = None
        self.visited = None
        self.recipient = None
        self.leaver = None
        self.voter = None
        self.verdict = None
        self.revived = None
        self.witched = None
        self.witch_target = None
        self.witcher = None
        self.amne = None
        self.remembered = None
        self.converted = None
        self.transported = None
        self.revealer = None

        broken_roles = ["Potion Master"]

        if '<span class="time night">Night' in message:
            self.type = "Night"
            self.night = int(message.split(
                "</span>")[0].split('<span class="time night">Night ')[1])

        elif '<span class="time day">Day' in message:
            self.type = "Day"
            self.day = int(message.split("</span>")
                           [0].split('<span class="time day">Day ')[1])

        elif '<span class="stage">Defense</span>' in message:
            self.type = "Defense"

        elif '<span class="stage">Judgement</span>' in message:
            self.type = "Judgement"

        elif " investigated " in message and ('<span class="notice Investigator"' in message or ('<span class="notice ' in message and 'Investigator" title="' in message)):
            self.type = "Investigation"
            visitor = message.split(">")[1].split(" investigated ")[0]
            try:
                self.visitor = _get_player(visitor, all_players)
            except ValueError:
                visitor = visitor.replace(
                    " ", "") if visitor in broken_roles else visitor
                self.visitor = _get_player(visitor, all_players)
            self.visited = _get_player(message.split(
                ".</span>")[0].split(" investigated ")[1], all_players)

        elif '<span class="notice Sheriff"' in message or ('<span class="notice ' in message and 'Sheriff" title="' in message) and ' checked ' in message:
            self.type = "Sheriff"
            try:
                visited = message.split(".</span>")[0].split(" checked ")[1]
            except IndexError:
                visited = ""
            try:
                visitor = message.split(">")[1].split(" checked ")[0]
            except IndexError:
                visitor = ""
            self.visitor = _get_player(visitor, all_players)
            self.visited = _get_player(visited, all_players)

        elif 'whisper" title="' in message or 'whisper">' in message:
            self.type = "Whisper"
            author = message.split(' ">')[0].split(" ")[-2]
            recipient = message.split(' ">')[0].split(" ")[-1]

            try:
                self.author = _get_player(author, all_players)
            except ValueError:
                author = message.split(' ">')[0].split(
                    " ")[-2] + " " + message.split(' ">')[0].split(" ")[-1]
                self.author = _get_player(author, all_players)

            try:
                self.recipient = _get_player(recipient, all_players)
            except ValueError:
                try:
                    recipient = message.split(' ">')[0].split(
                        " ")[-2] + " " + message.split(' ">')[0].split(" ")[-1]
                    self.recipient = _get_player(
                        recipient, all_players)
                except ValueError:
                    recipient = message.split(
                        '">')[1].split(" to ")[1].split(": ")[0]
                    self.recipient = _get_player(
                        recipient, all_players)

            try:
                self.message = message.split(
                    ":", 1)[1].split("</span>")[0].strip()
            except IndexError:
                self.message = ""

        elif '<span class="notice"' in message and "attacked by" in message:
            self.type = "Death"
            if " was attacked by" in message:
                killed = message.split('">')[1].split(" was attacked by")[0]
                self.killed = _get_player(killed, all_players)

            else:
                self.killed = _get_player(message.split(
                    '">')[1].split(" attacked by")[0], all_players)
            self.killer = message.split(".</span>")[0].split(" ")[-1]

        elif '<span class="notice"' in message and ' was ignited by an Arsonist.</span>' in message:
            self.type = "Death"
            self.killer = "Arsonist"
            killed = message.split('">')[1].split(
                " was ignited by an Arsonist.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and "visited a VampireHunter.</span>" in message:
            self.type = "Death"
            self.killer = "VampireHunter"
            killed = message.split('">')[1].split(
                " visited a VampireHunter.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and " was staked by a VampireHunter.</span>" in message:
            self.type = "Death"
            self.killer = "VampireHunter"
            killed = message.split('">')[1].split(
                " was staked by a VampireHunter.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and "died guarding someone.</span>" in message:
            self.type = "Death"
            self.killer = "Guarding"
            killed = message.split('">')[1].split(
                " died guarding someone.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and " died from guilt over shooting a Town member.</span>" in message:
            self.type = "Death"
            self.killer = "Guilt"
            killed = message.split('">')[1].split(
                " died from guilt over shooting a Town member.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and "visited a SerialKiller.</span>" in message:
            self.type = "Death"
            self.killer = "SerialKiller"
            killed = message.split('">')[1].split(
                " visited a SerialKiller.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice' in message and ' has been lynched.</span>' in message:
            self.type = "Death"
            self.killer = "Lynch"
            killed = message.split('">')[1].split(
                " has been lynched.</span>")[0]
            try:
                self.killed = _get_player(killed, all_players)
            except ValueError:
                killed = killed.replace(
                    " ", "") if killed in broken_roles else killed
                self.killed = _get_player(killed, all_players)

        elif '<span class="notice Jailor ' in message and ' decided to execute ' in message:
            self.type = "Death"
            self.killer = "Jailor"
            killed = message.split(" decided to execute ")[
                1].split('.</span>')[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and ' died from heartbreak.</span>' in message:
            self.type = "Death"
            self.killer = "Heartbreak"
            killed = message.split('">')[1].split(
                " died from heartbreak.</span>")[0]
            self.killed = _get_player(killed, all_players)

        elif '<span class="notice"' in message and "has left the game.</span>" in message:
            self.type = "Quit"
            player = message.split('">')[1].split(
                " has left the game.</span>")[0]
            self.leaver = _get_player(player, all_players)

        elif '<span class="notice"' in message and 'voted guilty.</span>' in message or 'voted innocent.</span>' in message or 'abstained.</span>' in message:
            self.type = "Vote"

            verdict = message.split('.</span>')[0].split(" ")[-1]
            voter = message.split('">')[1]
            if verdict == "abstained":
                self.verdict = "Abstain"
                self.voter = voter.split(" abstained.</span>")[0]
            if verdict == "guilty":
                self.verdict = "Guilty"
                self.voter = voter.split(" voted guilty.</span>")[0]
            if verdict == "innocent":
                self.verdict = "Innocent"
                self.voter = voter.split(" voted innocent.</span>")[0]

        elif '<span class="notice' in message and 'has been resurrected.</span>' in message:
            self.type = "Revive"
            revived = message.split(
                " has been resurrected.</span>")[0].split('">')[1]
            self.revived = _get_player(revived, all_players)

        elif '<span class="notice' in message and 'Witch control"' in message:
            self.type = "Witch"
            self.witcher = message.split('">')[1].split(" ")[0]
            msg = message.split(f'">{self.witcher} made ')[
                1].split(" target ")
            try:
                self.witched = _get_player(msg[0], all_players)
            except ValueError:
                try:
                    msg = message.split(f'">{self.witcher} made ')[
                        1].rsplit(" target ")
                    self.witched = _get_player(msg[0], all_players)
                except ValueError:
                    msg[0] = msg[0].replace(
                        " ", "") if msg[0] in broken_roles else msg[0]
                    self.witched = _get_player(msg[0], all_players)

            self.witch_target = _get_player(
                msg[-1].split(".</span>")[0], all_players)

        elif '<span class="notice"' in message and " has remembered they were " in message:
            self.type = "Remember"
            self.remembered = message.split(".</span>")[0].split(" ")[-1]
            amne = message.split('">')[1].split(
                " has remembered they were ")[0]
            self.amne = _get_player(amne, all_players)

        elif '<span class="notice Vampire convert"' in message:
            self.type = "Conversion"
            converted = message.split('">')[1].split(
                " was converted from being ")[0]
            self.converted = _get_player(converted, all_players)

        elif '<span class="notice' in message and '">Transporter swapped ' in message:
            self.type = "Transport"
            msg = message.split('">Transporter swapped ')[1].split(" with ")
            transported1 = _get_player(msg[0], all_players)
            try:
                transported2 = _get_player(
                    msg[1].split(".</span>")[0], all_players)
            except ValueError:
                msg = message.split('">Transporter swapped ')[
                    1].rsplit(" with ")
                transported2 = _get_player(
                    msg[0].split(".</span>")[0], all_players)
            self.transported = [transported1, transported2]

        elif '<span class="notice"' in message and "has revealed themselves as the Mayor.</span>" in message:
            self.type = "Reveal"
            revealer = message.split('">')[1].split(
                " has revealed themselves as the Mayor.</span>")[0]
            self.revealer = _get_player(revealer, all_players)

        else:
            self.type = "Message"

            self.is_mafia = bool('mafia">' in message)

            self.is_jail = bool('jail">' in message)

            try:
                name = message.split('<span class="')[1].split(" ")[0]
            except IndexError:
                name = ""
            try:
                author = _get_player(name, all_players)
            except ValueError:
                name = message.split('<span class="')[1].split(
                    " ")[0] + " " + message.split('<span class="')[1].split(" ")[1]
                author = _get_player(name, all_players)

            try:
                details = message.split(": ")[1]
                details = details.split("</span>")[0]
            except IndexError:
                details = ""

            self.author = author
            self.message = details

            # Unescape HTML
            self.message = self.message.replace("&gt;", ">").replace(
                "&amp;", "&") if self.message else self.message

    def __repr__(self):
        return self.type


class Player:
    """
    Represents a player in the game.

    Attributes
    -------------
    name: :class:`str`
        The player's username
    nick: :class:`str`
        The player's in game name
    slot: :class:`int`
        The player's slot (between 1 and 15)
    role: :class:`str`
        The player's role, e.g Mafioso
    faction: :class:`str
        The player's faction, e.g Mafia
    alignment: :class:`str`
        The player's alignment, e.g Mafia Killing
    """

    def __init__(self, data):
        name = data['name']

        category = data['type']

        all_players = data['all_players']

        all_players = json.loads(all_players)["players"]

        for player in all_players:
            if player[category] == name:
                info = player
                break

        role_info = _find_faction(info["role"])

        self.name = info["username"]
        self.role = info["role"]
        self.slot = int(info["slot"])
        self.nick = info["ign"]
        self.faction = role_info["faction"]
        self.alignment = role_info["alignment"]

    def __repr__(self):
        return self.nick


def _find_faction(role):

    if role == "BodyGuard":
        role_info = {"faction": "Town", "alignment": "Town Protective"}
    elif role == "Doctor":
        role_info = {"faction": "Town", "alignment": "Town Protective"}
    elif role == "Escort":
        role_info = {"faction": "Town", "alignment": "Town Support"}
    elif role == "Investigator":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}
    elif role == "Jailor":
        role_info = {"faction": "Town", "alignment": "Town Killing"}
    elif role == "Lookout":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}
    elif role == "Mayor":
        role_info = {"faction": "Town", "alignment": "Town Support"}
    elif role == "Medium":
        role_info = {"faction": "Town", "alignment": "Town Support"}
    elif role == "Retributionist":
        role_info = {"faction": "Town", "alignment": "Town Support"}
    elif role == "Sheriff":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}
    elif role == "Spy":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}
    elif role == "Transporter":
        role_info = {"faction": "Town", "alignment": "Town Support"}
    elif role == "VampireHunter":
        role_info = {"faction": "Town", "alignment": "Town Killing"}
    elif role == "Veteran":
        role_info = {"faction": "Town", "alignment": "Town Killing"}
    elif role == "Vigilante":
        role_info = {"faction": "Town", "alignment": "Town Killing"}
    elif role == "Crusader":
        role_info = {"faction": "Town", "alignment": "Town Protective"}
    elif role == "Tracker":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}
    elif role == "Trapper":
        role_info = {"faction": "Town", "alignment": "Town Protective"}
    elif role == "Psychic":
        role_info = {"faction": "Town", "alignment": "Town Investigative"}

    elif role == "Blackmailer":
        role_info = {"faction": "Mafia", "alignment": "Mafia Support"}
    elif role == "Consigliere":
        role_info = {"faction": "Mafia", "alignment": "Mafia Support"}
    elif role == "Consort":
        role_info = {"faction": "Mafia", "alignment": "Mafia Support"}
    elif role == "Disguiser":
        role_info = {"faction": "Mafia", "alignment": "Mafia Deception"}
    elif role == "Forger":
        role_info = {"faction": "Mafia", "alignment": "Mafia Deception"}
    elif role == "Framer":
        role_info = {"faction": "Mafia", "alignment": "Mafia Deception"}
    elif role == "Godfather":
        role_info = {"faction": "Mafia", "alignment": "Mafia Killing"}
    elif role == "Janitor":
        role_info = {"faction": "Mafia", "alignment": "Mafia Deception"}
    elif role == "Mafioso":
        role_info = {"faction": "Mafia", "alignment": "Mafia Killing"}
    elif role == "Hypnotist":
        role_info = {"faction": "Mafia", "alignment": "Mafia Deception"}
    elif role == "Ambusher":
        role_info = {"faction": "Mafia", "alignment": "Mafia Support"}

    elif role == "Amnesiac":
        role_info = {"faction": "Neutral", "alignment": "Neutral Benign"}
    elif role == "Arsonist":
        role_info = {"faction": "Neutral", "alignment": "Neutral Killing"}
    elif role == "Executioner":
        role_info = {"faction": "Neutral", "alignment": "Neutral Evil"}
    elif role == "Guardian Angel":
        role_info = {"faction": "Neutral", "alignment": "Neutral Benign"}
    elif role == "Jester":
        role_info = {"faction": "Neutral", "alignment": "Neutral Evil"}
    elif role == "Juggernaut":
        role_info = {"faction": "Neutral", "alignment": "Neutral Killing"}
    elif role == "Pirate":
        role_info = {"faction": "Neutral", "alignment": "Neutral Chaos"}
    elif role == "Plaguebearer":
        role_info = {"faction": "Neutral", "alignment": "Neutral Chaos"}
    elif role == "SerialKiller":
        role_info = {"faction": "Neutral", "alignment": "Neutral Killing"}
    elif role == "Survivor":
        role_info = {"faction": "Neutral", "alignment": "Neutral Benign"}
    elif role == "Vampire":
        role_info = {"faction": "Neutral", "alignment": "Neutral Chaos"}
    elif role == "Werewolf":
        role_info = {"faction": "Neutral", "alignment": "Neutral Killing"}
    elif role == "Witch":
        role_info = {"faction": "Neutral", "alignment": "Neutral Evil"}

    elif role in ["Coven Leader", "Potion Master", "HexMaster", "Necromancer", "Poisoner", "Medusa"]:
        role_info = {"faction": "Coven", "alignment": "Coven"}

    return role_info
