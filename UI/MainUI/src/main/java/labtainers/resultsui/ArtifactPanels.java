/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package labtainers.resultsui;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JComboBox;
import javax.swing.JTextField;
import static labtainers.resultsui.ParamReferenceStorage.LOG_ACCESIBLE_FieldType;
import static labtainers.resultsui.ParamReferenceStorage.LOG_TS_ACCESSIBLE_LineType;
import static labtainers.resultsui.ParamReferenceStorage.LineType_ITEMS;
import static labtainers.resultsui.ParamReferenceStorage.SpecialTimeStampType;
import static labtainers.resultsui.ParamReferenceStorage.justFieldType;
import static labtainers.resultsui.ParamReferenceStorage.lineParamAccessible;
import static labtainers.resultsui.ParamReferenceStorage.timeStampDelimiterAccessible;
import labtainers.resultsui.ToolTipHandlers.ToolTipWrapper;

/**
 *
 * @author student
 */
public class ArtifactPanels extends javax.swing.JPanel {

    /**
     * Creates new form ArtifactsPanel
     */
    public ArtifactPanels() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel3 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        UpButton = new javax.swing.JButton();
        DownButton = new javax.swing.JButton();
        ArtifactPanel = new javax.swing.JPanel();
        TagTextField = new javax.swing.JTextField();
        ContainerComboBox = new javax.swing.JComboBox<>();
        FileTextField = new javax.swing.JTextField();
        FieldTypeComboBox = new javax.swing.JComboBox<>();
        FieldIDTextField = new javax.swing.JTextField();
        LineTypeComboBox = new javax.swing.JComboBox<>();
        LineIDTextField = new javax.swing.JTextField();
        TimeStampComboBox = new javax.swing.JComboBox<>();
        TimeDelimiterTextField = new javax.swing.JTextField();

        setBorder(javax.swing.BorderFactory.createEtchedBorder());
        setMaximumSize(new java.awt.Dimension(1560, 86));
        setMinimumSize(new java.awt.Dimension(1560, 86));
        setName(""); // NOI18N
        setPreferredSize(new java.awt.Dimension(1560, 86));

        jLabel3.setFont(new java.awt.Font("Ubuntu", 1, 48)); // NOI18N
        jLabel3.setText("10");

        jButton1.setText("Delete");

        UpButton.setFont(new java.awt.Font("Ubuntu", 0, 15)); // NOI18N
        UpButton.setText("^");
        UpButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                UpButtonActionPerformed(evt);
            }
        });

        DownButton.setFont(new java.awt.Font("Ubuntu", 0, 15)); // NOI18N
        DownButton.setText("V");
        DownButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                DownButtonActionPerformed(evt);
            }
        });

        ArtifactPanel.setBorder(javax.swing.BorderFactory.createEmptyBorder(1, 1, 1, 1));

        FieldTypeComboBox.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                FieldTypeComboBoxItemStateChanged(evt);
            }
        });

        FieldIDTextField.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createEtchedBorder(), "Field ID"));

        LineTypeComboBox.setToolTipText("Identifies how the line is to be identified");
        LineTypeComboBox.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createEtchedBorder(), "Line Type"));
        LineTypeComboBox.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                LineTypeComboBoxItemStateChanged(evt);
            }
        });

        LineIDTextField.setToolTipText("Parameter based on Line Type");
        LineIDTextField.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createEtchedBorder(), "Line ID"));

        TimeStampComboBox.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createEtchedBorder(), "Timestamp Type"));
        TimeStampComboBox.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                TimeStampComboBoxItemStateChanged(evt);
            }
        });

        TimeDelimiterTextField.setHorizontalAlignment(javax.swing.JTextField.LEFT);
        TimeDelimiterTextField.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createEtchedBorder(), "Time Delimiter"));
        TimeDelimiterTextField.setMinimumSize(new java.awt.Dimension(20, 100));

        javax.swing.GroupLayout ArtifactPanelLayout = new javax.swing.GroupLayout(ArtifactPanel);
        ArtifactPanel.setLayout(ArtifactPanelLayout);
        ArtifactPanelLayout.setHorizontalGroup(
            ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(ArtifactPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(TagTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(ContainerComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 116, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(FileTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 138, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(FieldTypeComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 160, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(FieldIDTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(LineTypeComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 165, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(LineIDTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 142, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(TimeStampComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 143, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(TimeDelimiterTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 124, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        ArtifactPanelLayout.setVerticalGroup(
            ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                .addComponent(TimeDelimiterTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addComponent(TimeStampComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addComponent(LineIDTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addComponent(LineTypeComboBox)
                .addComponent(FieldIDTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addGroup(ArtifactPanelLayout.createSequentialGroup()
                .addGroup(ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(FileTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(FieldTypeComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(ArtifactPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(TagTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(ContainerComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(0, 0, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(this);
        this.setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel3)
                .addGap(6, 6, 6)
                .addComponent(ArtifactPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(DownButton, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(UpButton, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(6, 6, 6)
                                .addComponent(UpButton)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(DownButton))
                            .addGroup(layout.createSequentialGroup()
                                .addContainerGap()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(ArtifactPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel3))))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addComponent(jButton1, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
    }// </editor-fold>//GEN-END:initComponents

    private void UpButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_UpButtonActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_UpButtonActionPerformed

    private void DownButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_DownButtonActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_DownButtonActionPerformed

    private void FieldTypeComboBoxItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_FieldTypeComboBoxItemStateChanged
        fieldTypeListener();
    }//GEN-LAST:event_FieldTypeComboBoxItemStateChanged

    private void LineTypeComboBoxItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_LineTypeComboBoxItemStateChanged
        lineTypeListener();
    }//GEN-LAST:event_LineTypeComboBoxItemStateChanged

    private void TimeStampComboBoxItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_TimeStampComboBoxItemStateChanged
        timeStampListener();
    }//GEN-LAST:event_TimeStampComboBoxItemStateChanged

        //The listeners sees what values are present in their respective fields and then changes the interface based on that(remove or adding other fields)
    private void lineTypeListener(){
        ToolTipWrapper lineType = (ToolTipWrapper)LineTypeComboBox.getSelectedItem();
        
        if(lineType.getItem().equals("NONE")){
            LineIDTextField.setVisible(false);
        }
        else
            LineIDTextField.setVisible(true);
        

        //Does the line type allow for LOG_TS option in the TimeStampComboBox?
        if(LOG_TS_ACCESSIBLE_LineType.contains(lineType.getItem())){               
            //Add "LOG_TS" to the timestampComboBox if it's not already
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[0]) == -1)
                TimeStampComboBox.addItem(SpecialTimeStampType[0]);
        }
        else{
            ToolTipWrapper fieldTypeTTW = (ToolTipWrapper)FieldTypeComboBox.getSelectedItem();
            //Remove "LOG_TS" from the timestampComboBox if it's not already
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[0]) != -1 && !LOG_ACCESIBLE_FieldType.contains(fieldTypeTTW.getItem()))
                TimeStampComboBox.removeItem(SpecialTimeStampType[0]);
        }
        
        this.revalidate();
        this.repaint();
    }
    
    private void fieldTypeListener(){  
        ToolTipWrapper fieldType = (ToolTipWrapper)FieldTypeComboBox.getSelectedItem();

        //Does the fieldType allow for certain user inputs
        if(!justFieldType.contains(fieldType.getItem())){
            FieldIDTextField.setVisible(true);
            if(lineParamAccessible.contains(fieldType.getItem())){
                LineTypeComboBox.setVisible(true);
                LineIDTextField.setVisible(true);
            }
            else{
               setLineTypeComboBox(LineType_ITEMS[0]);
               LineTypeComboBox.setVisible(false);
               setLineIDTextField("");
               LineIDTextField.setVisible(false); 
            }         
        }
        else{
            setFieldIDTextField("");
            FieldIDTextField.setVisible(false);
            setLineTypeComboBox(LineType_ITEMS[0]);
            LineTypeComboBox.setVisible(false);
            setLineIDTextField("");
            LineIDTextField.setVisible(false);
        }
       
        /*
        If the selected Field Type allows for the "LOG_TS" and "LOG_RANGE" in the timeStampComboBox, 
        then make sure to add them if they aren't there already
        */
        if(LOG_ACCESIBLE_FieldType.contains(fieldType.getItem())){
            //Add "LOG_TS" to the timestampComboBox if it's not already
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[0]) == -1)
                TimeStampComboBox.addItem(SpecialTimeStampType[0]);
            //Add "LOG_RANGE" to the timestampComboBox if it's not already
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[1]) == -1)
                TimeStampComboBox.addItem(SpecialTimeStampType[1]);          
        }
        /*
        If the selcted Field Type doesn't allow for "LOG_TS" and "LOG_RANGE" in the timeStampComboBox, 
        then make sure to remove them if they're still in the box
        */
        else{
            ToolTipWrapper lineType = (ToolTipWrapper)LineTypeComboBox.getSelectedItem();
            //Remove "LOG_TS" from the timestampComboBox if it's not already
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[0]) != -1 && !LOG_TS_ACCESSIBLE_LineType.contains(lineType.getItem()))
                TimeStampComboBox.removeItem(SpecialTimeStampType[0]);
            //Remove "LOG_RANGE" from the timestampComboBox if it's there
            if(((DefaultComboBoxModel)TimeStampComboBox.getModel()).getIndexOf(SpecialTimeStampType[1]) != -1)
                TimeStampComboBox.removeItem(SpecialTimeStampType[1]);          
        }
        
        ArtifactPanel.revalidate();
        ArtifactPanel.repaint();
    }
    
    private void timeStampListener(){
        ToolTipWrapper timestamptype = (ToolTipWrapper)TimeStampComboBox.getSelectedItem();
        //Does the timestamp Type allow for Time Delimiter input
        if(timeStampDelimiterAccessible.contains(timestamptype.getItem()))
            TimeDelimiterTextField.setVisible(true);
        else{
            setTimeDelimiterTextField("");
            TimeDelimiterTextField.setVisible(false);
        }
        ArtifactPanel.revalidate();
        ArtifactPanel.repaint();
    }
    
    
    
        //Field Getters
    public JComboBox<String> getContainerComboBox(){
        return ContainerComboBox;
    }    
    public JTextField getFieldIDTextField(){
        return FieldIDTextField;
    }
    public JTextField getTagTextField(){
        return TagTextField;
    }
    public JTextField getFileTextField(){
        return FileTextField;
    }
    public JComboBox<ToolTipWrapper> getFieldTypeComboBox(){
        return FieldTypeComboBox;
    }
    public JTextField getLineIDTextField(){
        return LineIDTextField;
    }
    public JComboBox<ToolTipWrapper> getLineTypeComboBox(){
        return LineTypeComboBox;
    }    
    public JComboBox<ToolTipWrapper> getTimeStampComboBox(){
        return TimeStampComboBox;
    }
    public JTextField getTimeStampTextField(){
        return TimeDelimiterTextField;
    }

    //Field SETTERS
    private void setContainerComboBox(String v){
        ContainerComboBox.setSelectedItem(v);
    }    
    private void setFieldIDTextField(String v){
        FieldIDTextField.setText(v);
    }
    private void setTagTextField(String v){
        TagTextField.setText(v);
    }
    private void setFileTextField(String v){
        FileTextField.setText(v);
    }
    private void setFieldTypeComboBox(ToolTipWrapper v){
        FieldTypeComboBox.setSelectedItem(v);
    }
    private void setLineIDTextField(String v){
        LineIDTextField.setText(v);
    }
    private void setLineTypeComboBox(ToolTipWrapper v){
        LineTypeComboBox.setSelectedItem(v);
    }    
    private void setTimeStampComboBox(ToolTipWrapper v){
        TimeStampComboBox.setSelectedItem(v);
    }
    private void setTimeDelimiterTextField(String v){
        TimeDelimiterTextField.setText(v);
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel ArtifactPanel;
    private javax.swing.JComboBox<String> ContainerComboBox;
    private javax.swing.JButton DownButton;
    private javax.swing.JTextField FieldIDTextField;
    private javax.swing.JComboBox<ToolTipWrapper> FieldTypeComboBox;
    private javax.swing.JTextField FileTextField;
    private javax.swing.JTextField LineIDTextField;
    private javax.swing.JComboBox<ToolTipWrapper> LineTypeComboBox;
    private javax.swing.JTextField TagTextField;
    private javax.swing.JTextField TimeDelimiterTextField;
    private javax.swing.JComboBox<ToolTipWrapper> TimeStampComboBox;
    private javax.swing.JButton UpButton;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel3;
    // End of variables declaration//GEN-END:variables
}
