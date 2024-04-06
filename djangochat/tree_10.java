import java.util.Stack;
import java.util.Scanner;
public class tree_10 {
// linked list node for stack 
static class node{
node2 data;
node next;
node(node2 data){
this.data=data;
this.next=null;
}
}
// stack class 
static class stack{
static node head;
// isempty methods
public static boolean isEmpty(){
return head==null;
}
// push methods
public static void push(node2 data){
node newNode = new node(data);
if(isEmpty()){
head=newNode;
return;
}
newNode.next=head;
head=newNode;
}
// pop methods
public static node2 pop(){
if(isEmpty()){
head=null;
return null;
}
node2 ch=head.data;
head=head.next;
return ch;
}
// peek method
public static node2 peek(){
if(isEmpty()){
return null;
}
return head.data;
}
}
// linked list node for tree
static class node2{
char data;
node2 left;
node2 right;
node2(char data){
this.data=data;
this.left=null;
this.right=null;
}
}
// craeting tree class
static class treeClass{
// craeting method to build tree
public static node2 nodeCreationTree(String str){
node2 temp,temp1,temp2;
char ch;
stack s1=new stack();
for(int i=0;i<str.length();i++){
ch=str.charAt(i);
if(ch=='+' || ch=='-' || ch=='*' || ch=='/'){
temp2=s1.pop();
temp1=s1.pop();
temp=new node2(ch);
temp.left=temp1;
temp.right=temp2;
s1.push(temp);
}else{
temp=new node2(ch);
s1.push(temp);
}
}
temp=s1.pop();
return temp;
}
// preorder recursive method
public static void preorder(node2 root){
if(root==null){
return;
}
System.out.print(root.data+" ");
preorder(root.left);
preorder(root.right);
}
// inorder recursive method
public static void inorder(node2 root){
if(root==null){
return;
}
inorder(root.left);
System.out.print(root.data+" ");
inorder(root.right);
}// postorder recursive method
public static void postorder(node2 root){
if(root==null){
return;
}
postorder(root.left);
postorder(root.right);
System.out.print(root.data+" ");
}
/*============== non recursive traversals ================= */
// non recursive inorder
public static void inOrderNonRecursive(node2 root){
stack s1= new stack();
node2 newNode = root;
while(newNode!=null){
s1.push(newNode);
newNode= newNode.left;
}
while(!s1.isEmpty()){
newNode=s1.pop();
System.out.print(newNode.data+" ");
newNode= newNode.right;
while(newNode!=null){
s1.push(newNode);
newNode= newNode.left;
}
}
}
// non recursive preorder
public static void preOrderNonRecursive(node2 root){
stack s1= new stack();
node2 newNode=root;
while(newNode!=null){
System.out.print(newNode.data+" ");
s1.push(newNode);
newNode= newNode.left;
}
while(!s1.isEmpty()){
newNode=s1.pop();
newNode=newNode.right;
while(newNode!=null){
System.out.print(newNode.data+" ");
s1.push(newNode);
newNode=newNode.left;
}
}
}
// non recursive postorder
public static void postOrderNonRecursive(node2 root){
// stack s1= new stack();
// stack s2= new stack();
Stack<node2> s1= new Stack<>();
Stack<node2> s2= new Stack<>();
s1.push(root);
while(!s1.isEmpty()){
node2 newNode=s1.pop();
s2.push(newNode);
if(newNode.left!=null){
s1.push(newNode.left);
}
if(newNode.right!=null){
s1.push(newNode.right);
}
} 
while(!s2.isEmpty()){
System.out.print(s2.peek().data+" ");
s2.pop();
}
//st1.push(root);
}
// tree class end
}
/*------------------------------------------------------------------------------------ */
// main function
public static void main(String[] args) {
treeClass t= new treeClass();
Scanner pk = new Scanner(System.in);
String str="ab+cd-*a-";// postfix expression
node2 root=t.nodeCreationTree(str);
System.out.println("-------------- Recursive ---------------");
System.out.print("Postorder : ");
t.postorder(root);
System.out.print("\nInorder : ");
t.inorder(root);
System.out.print("\nPreorder : ");
t.preorder(root);
System.out.println();
System.out.println("\n-------------- Non-Recursive ---------------");
System.out.print("Postorder : ");
t.postOrderNonRecursive(root);
System.out.print("\nInorder : ");
t.inOrderNonRecursive(root);
System.out.print("\nPreorder : ");
t.preOrderNonRecursive(root);
}
}