/**
 * An Observer specifies a One-to-Many relationship between and object and its dependents.
 * Such that when an object changes state it notifies the other objects about the change.
 */

interface NotificationObserver {
  onMessage(message: Message): string;
}

interface Notify {
  sendMessage(message: Message): any;
}

class Message {
  message: string;

  constructor(message: string) {
    this.message = message;
  }

  getMessage(): string {
    return `${this.message} from publication`;
  }
}

class User implements NotificationObserver {
  element: Element;

  constructor(element: Element) {
    this.element = element;
  }

  onMessage(message: Message) {
    return (this.element.innerHTML += `<li>you have a new message - ${message.getMessage()}</li>`);
  }
}

class MailingList implements Notify {
  protected observers: User[] = [];

  notify(message: Message) {
    this.observers.forEach((observer) => {
      observer.onMessage(message);
    });
  }

  subscribe(observer: User) {
    this.observers.push(observer);
  }
  unsubscribe(observer: User) {
    this.observers = this.observers.filter(
      (subscriber) => subscriber !== observer
    );
  }

  sendMessage(message: Message) {
    this.notify(message);
  }
}

const messageInput: Element | null = document.querySelector(".message-input");

const user1: Element | null = document.querySelector(".user1-messages");
const user2: Element | null = document.querySelector(".user2-messages");

const u1 = new User(user1 as Element);
const u2 = new User(user2 as Element);

const subscribeU1: Element | null = document.querySelector(".user1-subscribe");
const subscribeU2: Element | null = document.querySelector(".user2-subscribe");

const unSubscribeU1: Element | null =
  document.querySelector(".user1-unsubscribe");
const unSubscribeU2: Element | null =
  document.querySelector(".user2-unsubscribe");

const sendBtn: Element | null = document.querySelector(".send-btn");

const mailingList = new MailingList();

mailingList.subscribe(u1);
mailingList.subscribe(u2);

if (subscribeU1) {
  subscribeU1.addEventListener("click", () => {
    mailingList.subscribe(u1);
  });
}

if (subscribeU2) {
  subscribeU2.addEventListener("click", () => {
    mailingList.subscribe(u2);
  });
}

if(unSubscribeU1)
unSubscribeU1.addEventListener("click", () => {
  mailingList.unsubscribe(u1);
});
if(unSubscribeU2)
unSubscribeU2.addEventListener("click", () => {
  mailingList.unsubscribe(u2);
});

if(sendBtn)
sendBtn.addEventListener("click", () => {
  // @ts-ignore
  mailingList.sendMessage(new Message(messageInput.value));
});
